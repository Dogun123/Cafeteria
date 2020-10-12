from flask import Flask, Blueprint, render_template,request,redirect,url_for,Response
from db_model.mysql import data_upload
from datetime import date
import json
from wtforms import TextField,Form,validators

menu_category = Blueprint('menu',__name__)

schools = ["교동초등학교",
          "솔밭초등학교",
          "개신초등학교",
          "풍광초등학교",
          "개신중학교"
         ]
          
class SearchForm(Form):
    autocomp = TextField('학교명', id='school_autocomplete')

@menu_category.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(schools), mimetype='application/json')

@menu_category.route('/',methods=['GET','POST'])
def menuhome():
    form = SearchForm(request.form)
    return render_template('menu.html',form=form)

@menu_category.route('/menulist',methods=['GET','POST'])
def menulist():
    school_name = request.args.get('autocomp')
    return render_template('menulist.html',school_name=school_name)
    


@menu_category.route('/menudate',methods=['GET','POST'])
def menudate():
    date = request.args.get('date')
    school_name = request.args.get('school_name')
    menus = data_upload(school_name,date)
    return render_template('menudate.html',menus=menus,today=date)



