from flask import Flask, render_template, request
from DS_retriever import retrieve_top_n_sites_businesses
import os

app = Flask(__name__)

@app.route('/')
def hello():
    q = request.args.get('q') or ''
    results = None
    if q:
        latitude = 44.338398
        longitude =  -75.919733
        n = 10
        (sites, businesses) = retrieve_top_n_sites_businesses(latitude, longitude, n, "most reviewed")
        return render_template('index.html', sites=sites, businesses=businesses, q=q)
    else:
        return render_template('index.html', results=results, q=q)
        
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))