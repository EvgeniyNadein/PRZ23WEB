from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run()