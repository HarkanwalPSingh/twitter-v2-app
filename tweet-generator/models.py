class NewsItem():
    def __init__(self, url, headlines, content, timestamp, tweeted):
        self.url = url
        self.headlines = headlines
        self.content = content
        self.timestamp = timestamp
        self.tweeted = tweeted

    def __repr__(self):
        return f"{self.url}\n{self.headlines}\n{self.content}\n{self.timestamp}\n{self.tweeted}\n"