# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import pymongo
from pymongo.errors import DuplicateKeyError
from itemadapter import ItemAdapter

import firebase_admin
from firebase_admin import firestore


class JsonWritePipeline:
    def open_spider(self, spider):
        self.file = open("news_items.jsonl", "w")
    
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item

class MongoPipeline:
    collection_name = "news_items"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGO_URI"),
            mongo_db = crawler.settings.get("MONGO_DATABASE", "items")
        )
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.collection_name].create_index("url", unique = True)
        self.db[self.collection_name].create_index({ "timestamp": -1 })
    
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        except DuplicateKeyError:
            pass
        return item

class FirestorePipeline:
    collection_name = "news_items"

    def __init__(self):
        self.app = firebase_admin.initialize_app()
    
    def open_spider(self, spider):
        self.db = firestore.client()

    def process_item(self, item, spider):
        document_id = item['headlines']
        doc_ref = self.db.collection("news_items").document(document_id)
        doc_ref.set(item, merge = True)
    
    def close_spider(self, spider):
        self.db.close()
    