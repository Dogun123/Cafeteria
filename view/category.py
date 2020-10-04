from flask import Flask, Blueprint, render_template,request

menu_category = Blueprint('menu',__name__)

@menu_category.route('/')
def menuhome():
    return render_template('menu.html')

@menu_category.route('/menulist')
def menulist():
    school_name = request.args.get('school_name')
    menus = []
    for i in range(10):
        menus.append("메뉴 {}".format(i))
    print(school_name)
    
    return render_template('menulist.html',menus=menus,school_name=school_name)


