from flask import Flask, Blueprint, render_template

menu_category = Blueprint('menu',__name__)

@menu_category.route('/')
def menuhome():
    return render_template('menu.html')



