import time
from flask import Flask

api = Flask(__name__)

@api.route('/time')
def get_current_time():
    return {'time': time.time()}

@api.route('/magicwords', methods=['POST'])
def get_magic_words():
  string = request.form['value']
  print(string) 
  return {'data': 'helloworld'} 
