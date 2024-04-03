#api.py

# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Assignment 9
# Due Date: April 04 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Pulls an api
# Brief Description of what this module does. Creates a class with an api
# Citations: In class
# Anything else that's relevant:

import requests
import json

class myAPI():

    response = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=SaiSUTX86CuRN2lqBeZHs5k12rGx5TyhxfnaMku5')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    