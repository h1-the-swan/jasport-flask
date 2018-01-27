import os, json
from flask import render_template, url_for, flash
# from ..models import EditableHTML

from . import main
from app import basedir


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/resume')
def resume():
    # resume_data_fname = basedir + url_for('main.static', filename='data/resume/resume-data.json')
    resume_data_fname = basedir + url_for('static', filename='data/resume/resume-data.json')
    with open(resume_data_fname, 'r') as f:
        resume_data = json.load(f)
    return render_template('main/resume.html', resume_data=resume_data)


# @main.route('/about')
# def about():
#     editable_html_obj = EditableHTML.get_editable_html('about')
#     return render_template('main/about.html',
#                            editable_html_obj=editable_html_obj)
