''' Author: Sadie Stokes '''
''' HW: Assignment 12 '''
''' Description: Stevens Repo '''

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/courses')
def courses():

    DB_FILE = '/Users/sasto/Desktop/810A/810_startup.db'

    query = """SELECT i.CWID, i.Name, i.Dept, g.Course, count(*) AS HW11_students FROM HW11_instructors i
            JOIN HW11_grades g on i.CWID=g.Instructor_CWID GROUP BY g.Course order by i.Name"""

    db = sqlite3.connect(DB_FILE)

    results = db.execute(query)

    #results = db.fetchall()

    data = [{'CWID': cwid, 'Name': name, 'Dept': Dept, 'Course': course, 'Students':count}
                for cwid, name, Dept, course, count in results]
    
    db.close()

    return render_template('courses.html',
                            title='Stevens Repository',
                            table_title="Number of completed courses by Student",
                            instructors=data)
app.run(debug=True)
            
