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
    """List All SQLite Tables"""
    return (
        f"Available SQLite Tables:<br/>"
        f"attendance_ncaa2015<br/>"
        f"attendance_ncaa2016<br/>"
        f"attendance_ncaa2017<br/>"
        f"attendance_ncaa2018<br/>"
        f"attendance_ncaa2019<br/>"
        f"Teams20152019<br/>"
    )

@app.route("/schoolsearch/<school_name>")
def returnSchoolData(school_name):
    session = Session(engine)    

    results = engine.execute("SELECT school,total_attendance FROM attendance_ncaa2015")
    session.close()

    school_data=[]
    for school,total_attendance in results:
        school_dict={}
        school_dict["school"] = school
        school_dict["total_attendance"]=total_attendance
        return jsonify(school_data)

if __name__ == '__main__': 
        app.run(debug=True)