from BaseAdvertising import BaseAdvertising
from Ad import Ad
from Advertiser import Advertiser

if __name__ == '__main__':
    baseAdvertising = BaseAdvertising()
    advertiser1 = Advertiser("name1")
    advertiser2 = Advertiser("name2")
    ad1 = Ad("title1", "img-url1", "link1", advertiser1)
    ad2 = Ad("title2", "img-url2", "link2", advertiser2)
    print(baseAdvertising.describeMe())
    print("description of ad2 is : " + ad2.describeMe())
    print("description of advertiser1 is : " + advertiser1.describeMe())
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad1.incClicks()
    ad2.incClicks()
    print("advertiser2 name is " + advertiser2.getName())
    advertiser2.setName("new name")
    print("advertiser2 new name is " + advertiser2.getName())
    print("ad1 clicks num is " + str(ad1.getClicks()))
    print("advertiser 2 clicks num is " + str(advertiser2.getClicks()))
    print("total system click is " + str(Advertiser.getTotalClicks()))
    print("advertiser help :\n" + Advertiser.help())