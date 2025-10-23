from flask import Blueprint,request

auth = Blueprint('auth', __name__)

@auth.route('/chatbot')
def login():
    return "<h1>chatbot</h1>"


        
