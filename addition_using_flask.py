
from flask import Flask, render_template, jsonify
app = Flask(__name__)



@app.route('/', methods=['POST'])
def home():
   return flask.render_template('addition.html')

@app.route('/get_numbers')
def get_values():
   value1 = request.form('val1')
   value2 = request.form('val2')
   return flask.jsonify({'data':f'<p>The result is: {value1+value2}</p>'})
