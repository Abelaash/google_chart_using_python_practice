## Problem Description
## Find out if there are any duplicate url used in the json placeholder photo data

import requests

url = 'https://jsonplaceholder.typicode.com/photos'

#getting the data about the photo
response = requests.get(url)

#reading the data into a variabke
json_data = response.json()

#create a list for storing the url of each photo
url_list = []
for photo in json_data:
    url_list.append(photo['url'])

#How many items are in the url list 
print(len(url_list))

#How many items are there if we turn that list into a set
print(len(set(url_list)))