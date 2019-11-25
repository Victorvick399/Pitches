from app import main
from flask import render_template

@main.route('/')
def index():
    return render_template('test.html')



