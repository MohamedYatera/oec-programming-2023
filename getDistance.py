from geopy.geocoders import Nominatim
from geopy import distance
import InfoExtractor


def getDistances(userlocation):
    facilitycoords = InfoExtractor.getinfo()[0]
    geolocator = Nominatim(user_agent="geoapiExercises")
    place1 = geolocator.geocode(userlocation)
    userlat, userlon = (place1.latitude), (place1.longitude)
    location1 = float(userlat), float(userlon)

    facilitydistances = []
    for facility in facilitycoords:
        facilitylocation = facility
        currentDist = distance.distance(location1, facilitylocation).km
        #print(currentDist, " kms")
        facilitydistances.append(currentDist)
    return facilitydistances

