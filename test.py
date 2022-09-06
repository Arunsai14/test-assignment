# python program to read json file
import json

def json_file():
    """
     Allow to read places.json file and find out the city
     along with the count of places_to_visit
     and save output in output.txt file, the content should be updated with latest content
    :return: list of cities with visited places count
    """
    with open('places.json') as json_file:
        citysdata = json.load(json_file)

    data = ''
    for city in citysdata['cities']:
        #print(city['name'].places)
        data = data + str(city['name']) + ' - ' + str(len(city['places_to_visit']))
        data = data + '\n'

    print(data)
    with open('output.txt', 'w') as f:
        f.write(data)


json_file()