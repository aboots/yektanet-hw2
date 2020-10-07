from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    totalSystemClicks = 0

    def __init__(self, name):
        super().__init__()
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    @staticmethod
    def getTotalClicks():
        return Advertiser.totalSystemClicks

    def describeMe(self):
        return "this class is made for advertisers!"

    @staticmethod
    def help():
        return "this class has name,clicks,id,views\n" + "and it has setter/getter methods" + "and it extends BaseAdvertising class"

    def incClicks(self):
        super().incClicks()
        Advertiser.totalSystemClicks += 1
