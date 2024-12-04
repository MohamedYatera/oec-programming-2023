from tkinter import *
from tkinter import ttk
from geopy.geocoders import Nominatim
from geopy import distance
import sorting
import getDistance as gd
import InteractiveMap as im

# user defined function
def get_dis():
    try:
         
        geolocator = Nominatim(user_agent="geoapiExercises")
         
        place1 = geolocator.geocode(str(e1.get()))
        place2 = geolocator.geocode(str(e2.get()))
 
 
        Loc1_lat,Loc1_lon = (place1.latitude),(place1.longitude)
        Loc2_lat,Loc2_lon = (place2.latitude),(place2.longitude)
 
        location1=(Loc1_lat,Loc1_lon)
        location2=(Loc2_lat,Loc2_lon)
 
        res = (str(distance.distance(location1, location2).km)+" Km")
 
        result.set(res)
    except:
        result.set("something went wrong")
 
def main():
    city = e1.get()
    facilitydistances = gd.getDistances(city)
    selected_symptom = symptoms.get()
    if selected_symptom != "":
        priority = symptom_priority[selected_symptom][0]
        unit = symptom_priority[selected_symptom][1]
        facility = symptom_priority[selected_symptom][2]
    else:
        print("Please select a symptom from the combobox")
    
    im.generate_map()
    

# object of tkinter
# with background set to light grey
master = Tk()
master.configure(bg='light grey')
master.title("Find Distance")
# Variable Classes in tkinter
result = StringVar();
 

Label(master, text="Enter your city: " , bg = "light grey").grid(row=1, sticky=W)
 
Label(master, text="Age :", bg = "light grey").grid(row=2, sticky=W)

Label(master, text="Symptoms :", bg = "light grey").grid(row=4, sticky=W)

Label(master, text="", textvariable=result,bg = "light grey").grid(row=4,column=1, sticky=W)
 
 
e1 = Entry(master,width = 50)
e1.grid(row=1, column=1)
e2 = Entry(master, width = 50)
e2.grid(row=2, column=1)

b1 = Button(master, text="Find Facilities", command=main, bg = "white")
b1.grid(row=1, column=2,columnspan=2, rowspan=2,padx=5, pady=5,)
 
#
symptom_priority = sorting.symptom_priority

# Create the combobox widget
symptoms = ttk.Combobox(master, values=list(symptom_priority.keys()), width=55)
symptoms.grid(row=4, column=1)



def set_variables():
    print()

        
mainloop()