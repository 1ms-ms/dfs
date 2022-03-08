from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

#connect to db
def db_connection():
    con = None
    try:
        con = sqlite3.connect("notes.sqlite")
    except sqlite3.error as errorcode:
        print(errorcode)
    return con

#List all the notes
@app.route("/", methods=["GET"])
def notes():
    note = None
    con = db_connection()
    cursor = con.cursor()
    cursor = con.execute("SELECT * FROM note")
    notes = [
        dict(id=row[0],content=row[1])
        for row in cursor.fetchall()
        ]
    if notes is not None:  
        con.close()
        return jsonify(notes) 
#Post a note with given id and content
@app.route("/create", methods=["POST"])
def notes_post():
    con = db_connection()
    cursor = con.cursor()

    new_content = request.json["content"]
    sql = """INSERT OR IGNORE INTO note (content)
        VALUES (?)"""
    cursor = cursor.execute(sql, (new_content,))
    con.commit()
    con.close()
    return "Success", 200

#Delete a note with given id
@app.route("/delete/<int:id>", methods=["DELETE"])
def notes_delete(id):
    con = db_connection()
    cursor = con.cursor()
       
    sql = """ DELETE FROM note WHERE id=? """
    con.execute(sql, (id,))
    con.commit()
    con.close()
    return "Deleted note with id: {} .".format(id), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
