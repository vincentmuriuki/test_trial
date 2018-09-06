from flask import Flask, jsonify

app = Flask(__name__) 
app.config[''] = 'choco'
app.config['SESSION_TYPE'] = 'filesystem'

from fast_food import api_endpoints
from fast_food import models


# Get all orders at /orders