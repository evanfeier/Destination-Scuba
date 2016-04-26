from flask import Flask, render_template, request
from DS_retriever import retrieve_top_n_sites_businesses
import os
import requests
import copy
import json

app = Flask(__name__)

@app.route('/')
def hello():
    q = request.args.get('q') or ''
    n = request.args.get('n') or 20
    n = max(int(n), 20)
    radius = request.args.get('r') or 45
    radius = max(int(radius), 45)
    radius = min(radius, 2261)
    results = None
    latitude = 30.5907759
    longitude = -96.4317468
    locationlist = []
    businesslist = []
    if q:
        str = q
        str.replace("%20", "+")
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+str)
        resp_json_payload = response.json()
        latitude = resp_json_payload['results'][0]['geometry']['location'].get("lat", "")
        longitude =  resp_json_payload['results'][0]['geometry']['location'].get("lng", "")
        sites = []
        businesses = []
        (sites, businesses) = retrieve_top_n_sites_businesses(latitude, longitude, n, "most reviewed", radius)
        while not sites and not businesses:
            radius = 2 * radius
            (sites, businesses) = retrieve_top_n_sites_businesses(latitude, longitude, n, "most reviewed", radius)
        locationlist = json.dumps(sites + businesses)
        
        return render_template('index.html', sites=sites, businesses=businesses, q=q, latitude=latitude, longitude=longitude, locationlist=locationlist, businesslist=businesslist, radius=radius)
    else:
        return render_template('index.html', results=results, q=q, latitude=latitude, longitude=longitude, locationlist=locationlist, businesslist=businesslist, radius=radius)
        
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
