import folium
import webbrowser
from geopy.geocoders import Nominatim
from geopy import distance
import getDistance as gd
import InfoExtractor as infoex


def generate_map():
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    distances = gd.getDistances('ottawa')
    facilityinfolists = infoex.getinfo()
    locations = facilityinfolists[0]
    beds = facilityinfolists[1]
    facilityname = facilityinfolists[2]
    opening = facilityinfolists[3]
    closing = facilityinfolists[4]
    contact = facilityinfolists[5]
    icu = facilityinfolists[6]
    ccu = facilityinfolists[7]
        

    m = folium.Map(location=(45.236261720838016, -78.47394518380646),zoom_start=4.8,width=800, height=400)

    #folium.Marker(location1, popup="Location 1").add_to(m)

    for i in range(len(locations)):
        folium.Marker(locations[i], popup=str(round(distances[i], 2)) + " km\n" + "Capacity: " + beds[i] + " Name : " + facilityname[i] 
        + ". ICU: " + icu[i] + ". CCU: " + ccu[i] + ". Hours : " + opening[i] + "/" + closing[i] + " Phone # :" + contact[i]).add_to(m)

    m.get_root().html.add_child(folium.Element("""
    <div>
    <h5>Interactive Map</h5><br/>
    </div>
    """
    ))

    m.save("output.html")
    webbrowser.open("output.html", new=2)  # open in new tab

