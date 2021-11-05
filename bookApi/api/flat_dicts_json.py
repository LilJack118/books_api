import requests
import json

url='https://www.googleapis.com/books/v1/volumes?q=war'
response = requests.get(url=url)
data = response.json()['items']

def flatten_dictionary(data, output):
    for key in data.keys():
        if type(data[key]) == dict:
            flatten_dictionary(data[key], output)
        else:
            output[key] = data[key]
    
    return output


def flatten_dictionaries_list(data):
    output_list = []
    for element in data:
        output = {}
        flatten_dictionary(element, output)
        output_list.append(output)
    
    return output_list


