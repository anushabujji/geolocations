from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd
import csv

# Create your views here.

def locations(request):
    return render(request, 'agent/index.html')


def agent_locations(request,city_id):
    if city_id == 1:
        actual_location = 'New York City'
    if city_id == 2:
        actual_location = 'Boston Massachusetts'
    if city_id == 3:
        actual_location = 'Los Angles California'
    if city_id == 4:
        actual_location = 'Chicago lllinois'
    if city_id == 5:
        actual_location = 'Houston Texas'
    if city_id == 6:
        actual_location = 'Phoenix,Arizona'
    if city_id == 7:
        actual_location = 'San Diego,California'
    if city_id == 8:
        actual_location = 'Dallas,Texas'
    if city_id == 9:
        actual_location = 'San Jose,California'
    if city_id == 10:
        actual_location = 'Austin'
    if city_id == 11:
        actual_location = 'Columbus,Ohio'
    geolocator = Nominatim(user_agent="anusha.upputholla@gmail.com")
    actual_locations = actual_location
    print(actual_location)
    location = geolocator.geocode(actual_location)
    location = (location.latitude, location.longitude)
    print(location)
    with open("C:\\Users\\Inthyd15523aupp1\\Desktop\\agents.tsv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        next(tsvreader)
        location_list = []
        for line in tsvreader:
            agent_location_str = " "
            agent_location = line[2:6]
            agent_name = line[1]
            agent_location = agent_location_str.join(agent_location)
            print(agent_location)
           
            try:
                age_location = geolocator.geocode(agent_location)
                location2 = (age_location.latitude, age_location.longitude)
                dix = distance.distance(location, location2).km
                new_agents_list = (agent_name, agent_location, dix)
                location_list.append(new_agents_list)
            except:
                pass
    df = pd.DataFrame(location_list, columns=[
                          'agent', 'address', 'distance'])
    df.sort_values(by=['distance'], inplace=True)
    df=df.head(10)
    df = df.T.to_dict().values()
    return render(request, 'agent/agent_locations.html', {'actual_location': actual_locations, 'df': df})
    # print("it will take 10 minutes time to print the data because so many records are there .")