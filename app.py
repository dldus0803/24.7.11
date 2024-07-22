from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import shutil

app = Flask(__name__)

@app.route('/elements', methods=['GET', 'POST'])
def elements():
    return render_template('elements.html')

@app.route('/generic', methods=['GET', 'POST'])
def generic():
    return render_template('generic.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

# @app.route('/', methods=['GET', 'POST'])
# def main():
#     return render_template('main.html', a = 0)

if __name__ == '__main__':
    app.run(debug=True)
