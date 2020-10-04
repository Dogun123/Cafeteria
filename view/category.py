from flask import Flask, Blueprint, render_template,request
from db_model.mysql import data_upload

menu_category = Blueprint('menu',__name__)

@menu_category.route('/')
def menuhome():
    return render_template('menu.html')

@menu_category.route('/menulist')
def menulist():
    school_name = request.args.get('school_name')
    menus = data_upload('solbat','20200103')
    
    return render_template('menulist.html',menus=menus,school_name=school_name)


