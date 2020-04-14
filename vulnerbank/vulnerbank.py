# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 17:37:29 2017

@author: firefly
"""

import simplejson
import requests
import psycopg2
import datetime

dnow=str(datetime.datetime.now())[0:10]

conn = psycopg2.connect("dbname='name' user='user' host='localhost' password='password'") # dummy data just to make the code awful


cur = conn.cursor()

def logon(id,pwd):
    try:
        sentence= "SELECT id,pass FROM logon WHERE id ='" + id + "' AND pass ='" + pwd + "'"
        print(sentence)    
        cur.execute(sentence) 
        #print(cur.query)
        res=cur.fetchall()     
       
        if(len(res)>=1):
            return(0,res[0][0].strip())
        else:
            return(1,"Incorrect login details")
    
    except psycopg2.Error as e:   
        conn.rollback()
        return (2,e.pgerror)


def accounts(user):
    l=[]
    try:
        s1="SELECT accnumber,balance FROM accounts WHERE id ='"+user+"'"  
        cur.execute(s1) 
        print(s1)
        res=cur.fetchall()
        for i in range (0,len(res)):
            l.append(res[i])
        return (l)
    except psycopg2.Error as e:   
        conn.rollback()
        return (2,e.pgerror)

def search(acc):
    l=[]
    try:
        s1="SELECT accnumber,balance FROM accounts WHERE accnumber ='"+acc+ "'"  
        cur.execute(s1) 
        print(s1)
        res=cur.fetchall()
        if(len(res)>0):
            for i in range (0,len(res)):
                l.append(res[i])
            return (0,l)
        else:
            return(1,'Account not found')
    except psycopg2.Error as e:   
        conn.rollback()
        return (2,e.pgerror)
