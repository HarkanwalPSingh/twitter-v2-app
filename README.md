# twitter-v2-app

## Commands

### Docker Commands

```shell
docker-compose up
docker-compose down
export MONGODB_VERSION=6.0-ubi8
docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server:$MONGODB_VERSION
```

### Scrapy Commands

```shell
export START_URLS="xxx"
export ALLOWED_DOMAINS="xxx"
scrapy crawl news-spider
```

### Vertex AI SDK for Python

#### Links

- [Vertex-Example-1](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/custom/sdk-custom-image-classification-online.ipynb)

```shell
pipenv install google-cloud-aiplatform google-cloud-storage firebase-admin
export PROJECT=xxx
export REGION=us-central1

```
