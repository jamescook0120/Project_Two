import numpy as np
from numpy.core.arrayprint import DatetimeFormat


import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///ncaafootball.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
# Station = Base.classes.station
# Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    # results = session.query(Measurement.date,Measurement.prcp).all()
 
    results = engine.execute('SELECT school,total_attendance FROM attendance_ncaa2015')

    session.close()

    # Convert list of tuples into normal list
    all_prcp = []
    for school,total_attendance in results:
        prcp_dict={}
        prcp_dict["school"]= school
        prcp_dict["total_attendance"]= total_attendance
        all_prcp.append(prcp_dict)
    
    return jsonify(all_prcp)


if __name__ == '__main__': 
        app.run(debug=True)