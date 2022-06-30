# ---- Import Dependencies ----
import datetime as dt
from secrets import token_bytes
from turtle import end_fill
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sympy import stationary_points

# ---- Setting up the Database -----
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

# save reference tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to the database
session = Session(engine)

# ---- Set up Flask -----
app = Flask(__name__)

# define stating point / routes
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Hawaii Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
