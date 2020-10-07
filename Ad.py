from BaseAdvertising import BaseAdvertising


class Ad(BaseAdvertising):
    def __init__(self, title, imgUrl, link, advertiser):
        super().__init__()
        self.title = title
        self.imgUrl = imgUrl
        self.link = link
        self.advertiser = advertiser

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getImgUrl(self):
        return self.imgUrl

    def setImgUrl(self, imgUrl):
        self.imgUrl = imgUrl

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link

    def setAdvertiser(self, advertiser):
        self.advertiser = advertiser

    def describeMe(self):
        return "This is class for Ad object"

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()


