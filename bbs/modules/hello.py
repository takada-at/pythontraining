#coding: utf-8

from flask import (
        Blueprint,
        render_template,
        )

module = Blueprint('hello', __name__)

@module.route('/')
def index():
    return render_template('hello_index.html')
