from django.http import Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render
from json import JSONDecodeError
from django.urls import reverse
import requests
import json

'''
TasteDive sample API endpoint:
url = "https://tastedive.com/api/similar?q=red+hot+chili+peppers%2C+pulp+fiction"

See documentation on: https://tastedive.com/read/api
'''

api_key = "447490-Similarl-CZJEL2ZA"

def index(request):
    return render(request, "main_app/index.html")

def search(request):
    if request.method == "GET":

        query = request.GET.get("query").lower()
        category = request.GET.get("category").lower()

        # Obtain API endpoint data
        data = requests.get(f"https://tastedive.com/api/similar?q={query}&type={category}&info=1&k={api_key}")

        if category == "any":
            data = requests.get(f"https://tastedive.com/api/similar?q={query}&info=1&k={api_key}")

        try:

            # Retrieve results 
            results = json.loads(data.text)
        
        except JSONDecodeError:
            raise HttpResponseServerError()

        return render(request, "main_app/search.html", {
            "results": results
        })

    else:
        return HttpResponseRedirect(reverse("index"))    


