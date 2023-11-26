class NewsItem():
    def __init__(self, url, headlines, content, timestamp):
        self.url = url
        self.headlines = headlines
        self.content = content
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.url}\n{self.headlines}\n{self.content}\n{self.timestamp}\n"