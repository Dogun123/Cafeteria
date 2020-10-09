from flask import Flask, Blueprint, render_template,request,redirect,url_for
from db_model.mysql import data_upload
from datetime import date

menu_category = Blueprint('menu',__name__)



@menu_category.route('/')
def menuhome():
    return render_template('menu.html')

@menu_category.route('/menulist',methods=['GET','POST'])
def menulist():
    school_name = request.args.get('school_name')
    return render_template('menulist.html',school_name=school_name)
    


@menu_category.route('/menudate',methods=['GET','POST'])
def menudate():
    date = request.args.get('date')
    school_name = request.args.get('school_name')
    menus = data_upload(school_name,date)
    return render_template('menudate.html',menus=menus,today=date)



