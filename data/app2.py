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

    results = engine.execute("SELECT school,id FROM Teams20152019 where school = ?",(school_name,))

    # results= engine.execute("""
# select * from (select a.id,a.school,a.Team,a.City,a.State,a.Current_Conference,b.total_attendance_all from (select * from Teams20152019)a,(select  id,school,sum(Total_attendance) as total_attendance_all from (select * from attendance_ncaa2015
# union all
# select * from attendance_ncaa2016
# UNION ALL
# select * from attendance_ncaa2017
# union ALL
# select * from attendance_ncaa2018
# union ALL
# select * from attendance_ncaa2019
# ) group by school order by id ) as b where a.id=b.id) where school = ?""",(school_name,))
    

    school_data=[]
    for school,id in results:
        school_dict={}
        school_dict["school"] = school
        school_dict["id"]=id
        school_data.append(school_dict)
        return jsonify(school_data)

    results_2 = engine.execute("SELECT * FROM attendence_ncaa2015 where id = ?",(school_dict["id"]))    
    results_3 = engine.execute("SELECT * FROM attendence_ncaa2016 where id = ?",(school_dict["id"]))
    results_4 = engine.execute("SELECT * FROM attendence_ncaa2017 where id = ?",(school_dict["id"])) 
    results_5 = engine.execute("SELECT * FROM attendence_ncaa2018 where id = ?",(school_dict["id"]))
    results_6 = engine.execute("SELECT * FROM attendence_ncaa2019 where id = ?",(school_dict["id"]))

    attendance_yoy=[]
    for total_attendance in results_2:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for total_attendance in results_3:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for total_attendance in results_4:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for total_attendance in results_5:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for total_attendance in results_6:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
        return jsonify(attendance_yoy)
    
    session.close()

if __name__ == '__main__': 
        app.run(debug=True)