import requests


def geocoding(geo_data):

    adress = f'{geo_data.adress.street}, {geo_data.adress.number} - {geo_data.adress.district}'
    response = requests.get(f'https://api.tomtom.com/search/2/geocode/{adress}.json?lat=37.337&lon=-121.89&key=Esq4YlvpAfdIgDTfFXnOSB7wEFyGe9t1')

    return response.json()['results'][0]['position']


def calculate_route(custumer, list_of_stores):
    customer_lat, custumer_lon = geocoding(custumer).values()
    stors = []

    for stor in list_of_stores:
        partner_lat, partner_lon = geocoding(stor).values()

        response = requests.get(f'https://api.tomtom.com/routing/1/calculateRoute//{customer_lat},{custumer_lon}:{partner_lat},{partner_lon}/json?instructionsType=text&language=en-US&vehicleHeading=90&sectionType=traffic&routeType=eco&traffic=true&avoid=unpavedRoads&travelMode=motorcycle&vehicleMaxSpeed=120&vehicleCommercial=false&vehicleEngineType=combustion&key=Esq4YlvpAfdIgDTfFXnOSB7wEFyGe9t1')
        response = response.json()

        lengthInMeters = response['routes'][0]['legs'][0]['summary']['lengthInMeters']

        handle_stor = {'id': stor.id, 'name': stor.name, 'lengthInMeters': lengthInMeters}

        stors.append(handle_stor)

    stors = sorted(stors, key=lambda k: k['lengthInMeters'])
    return stors
