from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("notes.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/notes", methods=["GET", "POST"])
def notes():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM note")
        notes = [
            dict(id=row[0],content=row[1])
            for row in cursor.fetchall()
        ]
        if notes is not None:
            return jsonify(notes)

    if request.method == "POST":
        new_id = request.form["id"]
        new_content = request.form["content"]
        sql = """INSERT INTO note (id, content)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_id, new_content))
        conn.commit()
        return f" successfully", 201


@app.route("/note/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_note(id):
    conn = db_connection()
    cursor = conn.cursor()
    note = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM note WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            note = r
        if note is not None:
            return jsonify(note), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE note
                SET id=?,
                    content=?,
                WHERE id=? """

        id = request.form["id"]
        content= request.form["content"]
        updated_note = {
            "id": id,
            "content": content,
        }
        conn.execute(sql, (id, content))
        conn.commit()
        return jsonify(updated_note)

    if request.method == "DELETE":
        sql = """ DELETE FROM note WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been ddeleted.".format(id), 200


if __name__ == "__main__":
    app.run(debug=True)
