
import requests
from bs4 import BeautifulSoup

import hotel
import latlong

session = requests.session()
# r = session.post("https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination=Uganda&latLong=51.470878%2C-0.449753&regionId=6000361&startDate=2017.10.21&endDate=2017.10.23&rooms=1&_xpid=11905%7C1&adults=1&timezoneOffset=32400000&siteid=16&langid=1033&hsrIdentifier=HSR")
# r = session.post("https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination=Uganda&latLong=51.470878%2C-0.449753&regionId=6000361&startDate=2017.10.21&endDate=2017.10.23&rooms=1&_xpid=11905%7C1&adults=1&timezoneOffset=32400000&siteid=16&langid=1033&hsrIdentifier=HSR")
# r = session.post("https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination=Entebbe%2C+Uganda&latLong=0.101592%2C32.494044&startDate=2017.10.21&endDate=2017.10.23&rooms=1&_xpid=11905%7C1&adults=1&timezoneOffset=32400000&siteid=16&langid=1033&hsrIdentifier=HSR")
# r = session.post("https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination=Entebbe%2C+Uganda&latLong=0.101592%2C32.494044&startDate=2017.10.21&endDate=2017.10.23&rooms=1&adults=1&timezoneOffset=32400000&langid=1033&hsrIdentifier=HSR")
# r = session.post("https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination=Entebbe%2C+Uganda&startDate=2017.10.21&endDate=2017.10.23&rooms=1&adults=1&timezoneOffset=32400000&langid=1033&hsrIdentifier=HSR")

if __name__ == '__main__':
    destination = raw_input("Destination: ")
    checkIn = raw_input("Checkin(yyy.mm.dd): ")
    checkOut = raw_input("Checkout()yyy.mm.dd: ")
    numberOfTraveller = raw_input("Number of Travellers: ")
    # sort = raw_input("Select how you want this sorted?\n 1. By price\n 2.By Distance from Downtown\n 3. By Guest Rating\n. 4. Recommend ")

    # if(sort == "1"):
    #     sort = "price"
    # elif (sort == "2"):
    #     sort = "distance"
    # elif ( sort== "3"):
    #     sort = "guestRating"
    # elif ( sort== "4"):
    #     sort = "recommend"
    #
    # url = "https://www.expedia.co.kr/Hotel-Search-Data?responsive=true&destination={0}&startDate={1}&endDate={2}&rooms=1&adults=1&sort=sort&timezoneOffset=32400000&siteid=16&langid=1033&hsrIdentifier=HSR&?1507581116345".format(
    #         destination, checkIn, checkOut, sort)
    hotel.scrapeHotels(destination, checkIn, checkOut)


















