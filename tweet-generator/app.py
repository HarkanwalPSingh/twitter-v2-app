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
    query = db.collection("news_items").order_by("timestamp", direction = firestore.Query.DESCENDING).limit(5)
    return query.get()

def generate_tweet(news_item: NewsItem):
    prompt = f"""
    Summarize the news content as a tweet, having relevant hashtags. Also provide the link to the original news.
    Headlines: {news_item.headlines}
    Content: {news_item.content}
    News Link: {news_item.url}"""
    return model.predict(prompt, **parameters)

def post_tweet(tweet):
    db.collection("news_items").document(news_item.headlines).update(
        {
            "tweeted": True
        }
    )

    print(tweet)


news_items = fetch_latest_news()

for news_item in news_items:
    news_item = NewsItem(**news_item.to_dict())
    if not news_item.tweeted:
        response = generate_tweet(news_item)
        tweet = response.text
        post_tweet(tweet)

db.close()