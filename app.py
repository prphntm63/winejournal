from flask import Flask
from .database import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'