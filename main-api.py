# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask,render_template, request,redirect, url_for,flash, send_from_directory
import os
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 

#Refresh cache
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function. 
  
@app.route("/")
def index():
    return render_template("/html/home.html")

@app.route('/about')
def about():
    return render_template("/html/about.html")

@app.route('/data')
def data():
    return render_template("/html/data.html")

@app.route('/contact')
def contact():
    return render_template("/html/contact.html")

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, port=port)
