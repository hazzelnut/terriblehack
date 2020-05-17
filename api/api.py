import time
from flask import Flask, request

api = Flask(__name__)

@api.route('/time')
def get_current_time():
    return {'time': time.time()}

@api.route('/magicwords', methods=['POST'])
def get_magic_words():
  data = request.get_json()
  value = data['value']

  # TODO: insert logic here
  print(value)

  # TODO: Input return value here
  magic_string = '123123'
  return {'data': magic_string}
