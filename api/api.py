import time
from flask import Flask, request

from antonym_generator import AntonymGenerator

app = Flask(__name__)
antonym_generator = AntonymGenerator()


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/magicwords', methods=['POST'])
def get_magic_words():
    data = request.get_json()
    value = data['value']

    ouput_string = antonym_generator.process_string(value)
    return {'data': ouput_string}
