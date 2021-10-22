from codecs import encode
from json.decoder import JSONDecodeError
from flask import Flask, render_template, request
import re
import json
import csv

from werkzeug.datastructures import FileStorage
app = Flask(__name__)  
app.secret_key = 'development key'  
 
@app.route('/', methods = ['GET','POST'])  
def accept_form():  
   return render_template('idea_form.html')  
 
 
@app.route('/csv_input',methods = ['GET','POST'])  
def input_csv(): 
   return render_template('csv_input.html')
 
@app.route('/tables',methods = ['GET','POST'])  
def create_tables(): 
   result_list = []
   csv_data = request.form["csv_text"]
   csv_rows = csv_data.split("\n")
   for row in csv_rows:

      row_values = row.split("¥")
      info_type = row_values[0]
      source = row_values[1]
      page = row_values[2]
      topic = row_values[3]
      summary = row_values[4]

      
      result_list.append(row_values)

   return render_template("tables.html", tables = result_list)  

if __name__ == '__main__':  
   app.run(debug = True)  