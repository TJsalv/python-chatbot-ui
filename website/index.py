from flask import Blueprint

index = Blueprint('views', __name__)

@index.route('/')
def home():
    return "<h1> PYTHON CHATBOT UNDER CONSTRUCTION <h1>"
