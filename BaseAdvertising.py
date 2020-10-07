class BaseAdvertising:
    idCounter = 1

    def __init__(self):
        self.id = BaseAdvertising.idCounter
        BaseAdvertising.idCounter += 1
        self.clicks = 0
        self.views = 0

    def getClicks(self):
        return self.clicks

    def incClicks(self):
        self.clicks += 1

    def incViews(self):
        self.views += 1

    def describeMe(self):
        return "This is class for BaseAdvertising"



