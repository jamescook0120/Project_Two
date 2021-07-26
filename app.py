import sqlalchemy
import datetime as dt
import pandas as pd
import json
import matplotlib.pyplot as plt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template,redirect


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///ncaafootball.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# print(Base.classes.keys())
# Save reference to the table
# Station = Base.classes.station
# Measurement = Base.classes.measurement

plotData = {
    'school_data':""
}
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    # Categorical data: Country names
    print(plotData['school_data'])
    years = ['2015', 'azil', 'Russia', 'Spain', 'UK', 'India']
    # Integer value interms of death counts
    totalAttendance = [112596, 37312, 5971, 27136, 40597, 7449]
    # Passing the parameters to the bar function, this is the main function which creates the bar plot
    plt.bar(years, totalAttendance)
    # Displaying the bar plot
    # plt.show()
    plt.savefig('static/images/plot.png')
    return render_template('index.html')


@app.route("/schoolsearch/<school_name>")
def returnSchoolData(school_name):
    conn=engine.connect() 
    # print(session)
    # print(engine)
    results = conn.execute("SELECT school,team,city,state,Current_Conference,id FROM Teams20152019 where school = ?",(school_name,))

    school_data=[]
    for school,team,city,state,Current_Conference,id in results:
        school_dict={}
        school_dict["school"] = school
        school_dict["team"] = team
        school_dict["city"] = city
        school_dict["state"]= state
        school_dict["Current_Conference"]= Current_Conference
        school_dict["id"]=id
        school_data.append(school_dict)
        # return jsonify(school_data)

    results_2 = conn.execute("SELECT year,total_attendance FROM attendance_ncaa2015 where id = ?",(school_data[0]["id"],))   
    results_3 = conn.execute("SELECT year,total_attendance FROM attendance_ncaa2016 where id = ?",(school_data[0]["id"],))
    results_4 = conn.execute("SELECT year,total_attendance FROM attendance_ncaa2017 where id = ?",(school_data[0]["id"],)) 
    results_5 = conn.execute("SELECT year,total_attendance FROM attendance_ncaa2018 where id = ?",(school_data[0]["id"],))
    results_6 = conn.execute("SELECT year,total_attendance FROM attendance_ncaa2019 where id = ?",(school_data[0]["id"],))
    # print(results_2)
    attendance_yoy=[]
    for year,total_attendance in results_2:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for year,total_attendance in results_3:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for year,total_attendance in results_4:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for year,total_attendance in results_5:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={}
    for year,total_attendance in results_6:
        attendance_dict={}
        attendance_dict["year"] = year
        attendance_dict["total_attendance"] = total_attendance
        attendance_yoy.append(attendance_dict)
        attendance_dict={} 
    conn.close()
    plotData['school_data']=jsonify(school_data,attendance_yoy)
    with open('data.json', 'w') as outfile:
        json.dump(plotData['school_data'], outfile)


    return redirect("/")


if __name__ == '__main__': 
        app.run(debug=True)
