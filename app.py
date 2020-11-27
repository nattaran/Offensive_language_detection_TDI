from flask import Flask, render_template, request, redirect,json,jsonify
import requests
from bokeh.plotting import figure,show,ColumnDataSource
from bokeh.embed import components
from bokeh.resources import INLINE
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import os

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['Get'])
def indexes():
    
        result = None
        #mystring = "Your Flight Information"

        return render_template('index3.html')
  
#@app.route('/FindDelay')
#def FindDelay():
#    flnum = request.args.get('flnum');
#    flac = request.args.get('flac');
#    prediction = 8.136;
#    return jsonify(result = 'The Flight Number you entered was ' + flac + flnum, prediction = "We predict %.2f minutes delay for this flight" %prediction);
    
  

#@app.route('/getMyJson')
#def getMyJson():
#    dataFrame = pd.read_csv("{{ url_for('static', filename='unique_carrier.csv') }}")
#    json = dataFrame.to_json(orient='records', date_format='iso')
#    response = Response(response=json, status=200, mimetype="application/json")
#    return(response)

  
if __name__ == '__main__':
	app.run(port=33507,debug=True)
