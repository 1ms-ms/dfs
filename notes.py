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
        return jsonify(notes)   
#Post a note with given id and content
@app.route("/create", methods=["POST"])
def notes_post():
    con = db_connection()
    cursor = con.cursor()

    new_id = request.form["id"]
    new_content = request.form["content"]
    sql = """INSERT OR IGNORE INTO note (id, content)
        VALUES (?, ?)"""
    cursor = cursor.execute(sql, (new_id, new_content))
    con.commit()
    return "Success", 200

#Delete a note with given id
@app.route("/delete/<int:id>", methods=["DELETE"])
def notes_delete(id):
    con = db_connection()
    cursor = con.cursor()
       
    sql = """ DELETE FROM note WHERE id=? """
    con.execute(sql, (id,))
    con.commit()
    return "Deleted note with id: {} .".format(id), 200


if __name__ == "__main__":
    app.run(debug=True)
