import requests


def geocoding(geo_data):

    if geo_data:
        adress = f"{geo_data['street']}, {geo_data['number']}-{geo_data['district']},{geo_data['city']} - {geo_data['state']}, {geo_data['cep']}"

        response = requests.get(f'https://api.tomtom.com/search/2/geocode/{adress}.json?lat=37.337&lon=-121.89&key=Esq4YlvpAfdIgDTfFXnOSB7wEFyGe9t1')

        coordinates = response.json()['results'][0]['position']

        return f"{coordinates['lat']},{coordinates['lon']}"


def calculate_route(customer, list_of_stores):

    customer = customer.adress.coordinates
    stors = []

    for stor in list_of_stores:

        response = requests.get(f'https://api.tomtom.com/routing/1/calculateRoute//{customer}:{stor.adress.coordinates}/json?instructionsType=text&language=en-US&vehicleHeading=90&sectionType=traffic&routeType=eco&traffic=true&avoid=unpavedRoads&travelMode=motorcycle&vehicleMaxSpeed=120&vehicleCommercial=false&vehicleEngineType=combustion&key=Esq4YlvpAfdIgDTfFXnOSB7wEFyGe9t1')
        response = response.json()

        lengthInMeters = response['routes'][0]['legs'][0]['summary']['lengthInMeters']

        handle_stor = {'id': stor.id, 'name': stor.name, 'lengthInMeters': lengthInMeters}

        stors.append(handle_stor)

    stors = sorted(stors, key=lambda k: k['lengthInMeters'])
    return stors
