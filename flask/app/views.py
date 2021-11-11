from app import app
from flask import Flask, render_template, Response

@app.route('/')
def home():
    return render_template('index.html')
