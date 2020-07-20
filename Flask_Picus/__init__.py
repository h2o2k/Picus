# This file is needed to run this application via a script in the main directory - Andrew

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

from Flask_Picus import routes
