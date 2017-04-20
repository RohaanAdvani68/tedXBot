import os
import sys
import json
from functions import *

import requests
from flask import Flask, request
import pyrebase

config = { #our config for our firebase app
    "apiKey": os.environ['FIREBASE_API_KEY'],
    "authDomain": os.environ['FIREBASE_AUTHDOMAIN'],
    "databaseURL": os.environ['FIREBASE_DATABASE_URL'],
    "storageBucket": os.environ['FIREBASE_STORAGE_BUCKET']
}

firebase = pyrebase.initialize_app(config) #initializes our firebase app, that can have database, auth, messaging etc.

auth = firebase.auth() #reference to the firebase app's authentication service
user = auth.sign_in_with_email_and_password(os.environ['FIREBASE_AUTH_EMAIL'], os.environ['FIREBASE_AUTH_PASSWORD']) # log the user of the database in

db = firebase.database() #grabbing the database in our firebase app

def checkDbFunctions():
    x=storeUser("XXX", db, user)
    u=getUser("XXX", db, user)
    r=removeUser("XXX", db, user)
    if x:   #x will be true if this user is already in database which should not be the case
        print "storeUser indicates that test user was already in database"
        return False
    if u is False:    #if user not found in database
        print "getUser indicates that test user not added to database"
        return False
    if r is False:
        print "removeUser indicates that test user was not in database to be removed"
        return False
    print "All g"
    return True

def test(x, y, message=""):
    if(x==y):
        return true
    else:
        print message
        return false

checkDbFunctions();
