# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for

from tebot import app


@app.route("/")
def index():
    return render_template('index.html')
