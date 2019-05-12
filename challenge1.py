# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:27:45 2017

@author: firefly
"""

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import vulnerbank as vb



app = Flask(__name__)


@app.route('/')

def welcome():
    return render_template('/main.html') 


 
@app.route ('/login', methods=['POST'])  
def login():

    user=request.form['form-username']
    pwd=request.form['form-password']
    d1,d2=vb.logon(user,pwd)
    
    if(d1==0):
        return redirect("/accounts&user="+d2)

    else:
        return render_template('main.html', err=d2)

@app.route('/accounts&user=<user>')
def accounts(user):
    l=vb.accounts(user)
    return render_template('accounts.html',user=user,l=l) 

@app.route ('/search', methods=['POST'])  
def search():
    acc=request.form['acc']
    d1,l=vb.search(acc)
    if(d1==0):
        return render_template('accounts2.html',l=l)
    else:
        return render_template('accounts3.html',err=l)


app.run(host='0.0.0.0', port=8081)
