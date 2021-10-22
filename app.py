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
 
 
 
@app.route('/download',methods = ['GET','POST'])  
def prepare_csv(): 

   regexes = request.form["regex_patterns"]
   strings = request.form["strings"]
   try:
      regex_json = json.loads(regexes)
      for obj in regex_json:
         test1 = obj["name"]
         test2 = obj["pattern"]
   except:
      return "Please ensure json is valid including 'name' and 'pattern' keys, and retry."
   results = {}
   for utt_string in strings.split("\n"):

      utt_string = utt_string.strip()
      utt_string = utt_string.lower()
      
      if utt_string == "":
         continue
      for pattern_object in regex_json:
   
         for pattern in pattern_object["pattern"]:
          
            # breakpoint()
            adapted_pattern = pattern.lower()
            
            adapted_pattern = "^" + adapted_pattern + "$"
            try: 
               if re.fullmatch(adapted_pattern, utt_string):
                  
                  if utt_string not in results.keys(): 
                     results[utt_string] = []
                     results[utt_string].append(["\"" + pattern + "\""])
                     results[utt_string].append(pattern_object["name"])
                  else:
                     if len(results[utt_string]) > 1:
                        if results[utt_string][1] == "":
                           results[utt_string][1] = pattern_object["name"]
                     results[utt_string][0].append("\"" + pattern + "\"")
                     
               else:
                  if utt_string not in results.keys():
                     results[utt_string] = []
                     results[utt_string].append([])
                     results[utt_string].append("")
                  else:
                     pass
            except:
               return f"Regex pattern <b>{pattern}</b> has an error. Fix and retry."
   def takeSecondLen(elem):
      return len(elem[1][0])
   result_list = []
   for key, val in results.items():
      result_list.append([key, val])
   result_list.sort(key=takeSecondLen)

   
      
               
            

   return render_template("results.html", patterns = result_list)  

if __name__ == '__main__':  
   app.run(debug = True)  