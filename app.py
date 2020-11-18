import os
from flask import (
    Flask, flash, render_template,
    redirect, request, sessions, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, check_password_harsh
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo =PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get_dish")
def get_dish():
    dish = mongo.db.dish.find()
    return render_template("recipes.html", dish=dish)


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template ("add.html")


if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
