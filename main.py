from flask import Flask,render_template,jsonify,request
from view import category


app = Flask(__name__, static_url_path = '/static')

app.register_blueprint(category.menu_category, url_prefix = '/menu')




@app.route('/')
def cover():
    return render_template('cover.html')


if __name__ == '__main__':
    app.run(host='localhost',port='5001',debug = True)