from flask import Flask, render_template, request

from mbta_finder import find_stop_near

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")
    


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        name = name.upper()
    return render_template("hello.html", name=name)

@app.route("/find/", methods=["GET", "POST"])
def find():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == "POST":
        requestedplace = str(request.form["Place, City, State"])
        requestedstop = find_stop_near(requestedplace)
        if stop:
            return render_template(
                "found.html", requestedstop=requestedstop, requestedplace=requestedplace
            )
        else:
            return render_template("find.html", error=True)
    return render_template("find.html", error=None)
