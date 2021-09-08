from flask import redirect, render_template, url_for, flash, request
from app import db
from .import bp as prod
from .models import Category

@prod.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    return render_template('addcategory.html.j2')