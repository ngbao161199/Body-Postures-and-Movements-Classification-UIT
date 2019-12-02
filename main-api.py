# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask,render_template, request,redirect, url_for,flash, send_from_directory, jsonify, make_response
from py_approach import DCSTree, LR, NB, knn
import json
import os
import pickle
import numpy
import csv
import pandas as pd

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
    return render_template("/html/home.html", 
    # data that contain algorithms value for linking it with 
    data=[{'algo':'Bernoulli_Naive_Bayes'}, {'algo':'Gaussian_Naive_Bayes'}, {'algo':'Decision_Tree'}, {'algo':'K_Neighrest_Neighbor'}, {'algo':'Logistic_Regression'}])

# result is the subsite that link directly to show result of algorihtm. 
@app.route("/result" , methods=['GET', 'POST'])
def result():
    # get algorithms value from the form that typing by users.
    select = request.form.get('algorithm')

    # for each algorithms chosen, link directly to subsite.
    if select == 'Decision_Tree':
        return jsonify("Fitting completed in: ", DCSTree.done, "Accuracy: ", DCSTree.acc, "MSE: ", DCSTree.mse, "Precision: ", DCSTree.precision, "Recall: ", DCSTree.recall)
    if select == 'Logistic_Regression':
        return jsonify("Fitting completed in: ", LR.done, "Accuracy: ", LR.acc,"MSE: ", LR.mse, "Precision: ", LR.precision, "Recall: ", LR.recall)
    if select == 'Gaussian_Naive_Bayes':
        return jsonify("Fitting completed in: ", NB.g_done, "Accuracy: ", NB.g_acc,"MSE: ", NB.g_mse, "Precision: ", NB.g_precision, "Recall: ", NB.g_recall)
    if select == 'Bernoulli_Naive_Bayes':
        return jsonify("Fitting completed in: ", NB.b_done, "Accuracy: ", NB.b_acc,"MSE: ", NB.b_mse, "Precision: ", NB.b_precision, "Recall: ", NB.b_recall)
    if select == 'K_Neighrest_Neighbor':
        return jsonify("Fitting completed in: ", knn.best_time, "Neighbor: ", knn.best_neighbor, "Accuracy: ", knn.best_accu, "MSE: ", knn.best_mse, "Precision: ", knn.best_precision, "Recall: ", knn.best_recall)
    else: return str(select)

# about subsite that show basic information about project and team member.
@app.route('/about')
def about():
    return render_template("/html/about.html")

# data visualization approach from Team 4. Generated from Jupyter Notebook.
@app.route('/data')
def data():
    return render_template("/html/data.html")

# Test Algorithm Site (Input manually by user)
@app.route("/algo")
def algo():
    return render_template('/html/algo.html', data=[{'math':'Bernoulli_Naive_Bayes'}, {'math':'Gaussian_Naive_Bayes'}, {'math':'Decision_Tree'}, {'math':'K_Neighrest_Neighbor'}, {'math':'Logistic_Regression'}])

# Test Algorithm Site (Input with file given by user)
@app.route("/algo_with_file")
def algo_with_file():
    return render_template('/html/algo_with_file.html' , data=[{'mul_math':'Bernoulli_Naive_Bayes'}, {'mul_math':'Gaussian_Naive_Bayes'}, {'mul_math':'Decision_Tree'}, {'mul_math':'K_Neighrest_Neighbor'}, {'mul_math':'Logistic_Regression'}])

@app.route("/testing", methods=['GET','POST'])
def testing():
    choosen = (int)(request.form.get('file'))
    choice = request.form.get('mul_math')
    if choice == 'Gaussian_Naive_Bayes':
        loaded_model = pickle.load(open('model/GaussianNB.sav', 'rb'))
        acc = NB.solve(choosen, loaded_model)
        acc = json.dumps(acc)
        return jsonify("Accuracy: ", acc)
    if choice == 'Bernoulli_Naive_Bayes':
        loaded_model = pickle.load(open('model/BernoulliNB.sav', 'rb'))
        acc = NB.solve(choosen, loaded_model)
        acc = json.dumps(acc)
        return jsonify("Accuracy: ", acc)
    if choice == 'Logistic_Regression':
        acc = LR.solve(choosen)
        acc = json.dumps(acc)
        return jsonify("Accuracy: ", acc)
    if choice == 'Decision_Tree':
        acc = DCSTree.solve(choosen)
        acc = json.dumps(acc)
        return jsonify("Accuracy: ", acc)
    if choice == 'K_Neighrest_Neighbor':
        acc = knn.solve(choosen)
        acc = json.dumps(acc)
        return jsonify("Accuracy: ", acc)

@app.route("/test",  methods=['GET','POST'])
def test():
    x1 = (float)(request.form.get('x1'))
    y1 = (float)(request.form.get('y1'))
    z1 = (float)(request.form.get('z1'))
    x2 = (float)(request.form.get('x2'))
    y2 = (float)(request.form.get('y2'))
    z2 = (float)(request.form.get('z2'))
    x3 = (float)(request.form.get('x3'))
    y3 = (float)(request.form.get('y3'))
    z3 = (float)(request.form.get('z3'))
    x4 = (float)(request.form.get('x4'))
    y4 = (float)(request.form.get('y4'))
    z4 = (float)(request.form.get('z4'))
    selection = request.form.get('math')
    if selection == 'Decision_Tree':
        dcs = DCSTree.predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
        dcs = dcs.tolist()
        dcs = json.dumps(dcs)
        return dcs
    if selection == 'Logistic_Regression':
        logic = LR.predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
        logic = logic.tolist()
        logic = json.dumps(logic)
        return logic
    if selection == 'Gaussian_Naive_Bayes':
        loaded_model = pickle.load(open('model/GaussianNB.sav', 'rb'))
        gnb = NB.predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4, loaded_model)
        gnb = gnb.tolist()
        gnb = json.dumps(gnb)
        return gnb
    if selection == 'Bernoulli_Naive_Bayes':
        loaded_model = pickle.load(open('model/BernoulliNB.sav', 'rb'))
        bnb = NB.predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4, loaded_model)
        bnb = bnb.tolist()
        bnb = json.dumps(bnb)
        return bnb
    if selection == 'K_Neighrest_Neighbor':
        neighbor_hell = knn.predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4)
        neighbor_hell = neighbor_hell.tolist()
        neighbor_hell = json.dumps(neighbor_hell)
        return neighbor_hell

@app.route('/contact')
def contact():
    return render_template('/html/contact.html')

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(debug=True, port=port)
