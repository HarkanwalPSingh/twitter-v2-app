import os
import firebase_admin
from firebase_admin import firestore
import vertexai
from vertexai.preview.language_models import TextGenerationModel
from models import NewsItem

app = firebase_admin.initialize_app()
db = firestore.client()

# Get project and location from environment variables
project = os.getenv('PROJECT')
location = os.getenv('LOCATION')

vertexai.init(project=project, location=location)
parameters = {
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison-32k")

def fetch_latest_news():
    query = db.collection("news_items").order_by("timestamp", direction = firestore.Query.DESCENDING).limit(1)
    return query.get()[0].to_dict()

def generate_tweet(news_item: NewsItem):
    prompt = f"""
    Summarize the news content as a tweet, having relevant hashtags. Also provide the link to the original news.
    Headlines: {news_item.headlines}
    Content: {news_item.content}
    News Link: {news_item.url}"""
    return model.predict(prompt, **parameters)

news_item = NewsItem(**fetch_latest_news())

response = generate_tweet(news_item)

print(response.text)

db.close()