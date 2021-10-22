from codecs import encode
from json.decoder import JSONDecodeError
from flask import Flask, render_template, request
import re
import json

from werkzeug.datastructures import FileStorage
app = Flask(__name__)  
app.secret_key = 'development key'  
 
@app.route('/', methods = ['GET','POST'])  
def accept_form():  
   return render_template('idea_form.html')  
 
 
 
@app.route('/tables',methods = ['GET','POST'])  
def create_tables(): 
   

   return render_template("tables.html", forms = result_list)  

if __name__ == '__main__':  
   app.run(debug = True)  