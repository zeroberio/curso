from flask import Flask, Request, response, redirect
app = Flask(__name__)

@app.route(‘/’)

def main():
 	return redirect(‘static/index.html’)