from flask import Flask, redirect, render_template, url_for, request, session
import random
import string

app = Flask(__name__)
app.secret_key = "secret_key"

events = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/newevent', methods=['GET','POST'])
def create_event():
    if "create" in request.form:
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        events[res] = {"title": request.form["ename"], "num": request.form['num'], "event": request.form["description"]}
        print(events[res])

        return f"Your event code is {res}"

    return render_template('newevent.html')


@app.route('/events/<evt>')
def event(evt):
    return events[evt]


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=True, port=80) 

