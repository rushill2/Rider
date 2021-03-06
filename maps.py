# file for threaded processes from flask
# initializes location and other data for use for
# other features
import fed
from geopy.geocoders import Nominatim

key = "AIzaSyAEGNwybqtkhb7f2HXEDGkWYqrkc9oRqNA"
INIT = (0,0)

# overseer of all things in this one
def acq(datag):
    loc = coordToPlace(datag.to_dict())
    print(loc)
    # fed.scrape(loc)

# find the smallest possible unit that would have some news
# Would likely have to scrap this due to api ratelimits
# Replace with recommendations for bikimg locations, and setting paths for those?
def coordToPlace(usedict):
        payload = ""
        global INIT
        blacklist = ['building', 'house', 'house_number', 'road', 'quarter']
        geolocator = Nominatim(user_agent="BikeTes")

        if('data[lat]' in usedict.keys() and 'data[lng]' in usedict.keys()):
            payload =usedict['data[lat]'] + "," + usedict['data[lng]']
        INIT = (float(usedict['data[lat]']), float(usedict['data[lng]']))
        print(usedict, INIT)
        loc = geolocator.reverse(payload)
        addr = loc.raw['address']
        # print(retloc)
        arr = list(addr.keys())

        # naive filtration
        if(all(x!=arr[1] for x in blacklist)):
            return addr[arr[1]]
        elif(all(x!=arr[2] for x in blacklist)):
            return addr[arr[2]]
        elif(all(x!=arr[3] for x in blacklist)):
            return addr[arr[3]]
        else:
            return addr[arr[4]]


# implement nearby biking suggestions

def testhelp(dataset):
    print(dataset)