import os
import datetime
from flask import Flask, render_template, request, request, Response, make_response  # from flask package get Flask class
from pymongo import MongoClient
from dotenv import load_dotenv
entries = []
load_dotenv()
def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGO_URI"))      #(os.environ.get("MONGO_URI"))
    app.db = client.Microblog
    @app.route("/", methods=["GET","POST"])
    def home():
        #global entries_list
        if request.method == "POST":
            entry_content = request.form.get("content")     #inserting from textarea
            entry_title = request.form.get("title")
            entry_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"title": entry_title,"content": entry_content, "date": entry_date })  #inserting records in Mongodb    #format_date = datetime.datetime.today().strptime(entry_date,"%Y-%m-%d").strftime("%b %d")
            entries.append((entry_title, entry_content,entry_date))
            print(entries) 
        list = [
                (entry["title"], entry["content"], entry["date"]) for entry in app.db.entries.find({})
                ]
        print(list)
        return render_template("index.html",entries = entries)  #, entries = database_list)          
    return app    
        
