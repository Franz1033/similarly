from django.shortcuts import render
import requests
import json

'''
See documentation on: https://tastedive.com/read/api
'''

# TasteDive API endpoint
url = "https://tastedive.com/api/similar?q=red+hot+chili+peppers%2C+pulp+fiction"

# Obtain the API data
data = requests.get(url)

# retrieve results using json.loads() function
results = json.loads(data.text)

def index(request):
    return render(request, "main_app/index.html", {
        "results": results
    })
