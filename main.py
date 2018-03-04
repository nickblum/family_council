from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/index/')
def overview():
    restaurants = session.query(Restaurant).all()
    return render_template('overview.html')

@app.route('/council/', methods=['GET','POST'])
def council():
    return render_template('council.html')

@app.route('/goals/', methods=['GET','POST'])
def goals():
    return render_template('goals.html')

@app.route('/history/', methods=['GET','POST'])
def history():
    return render_template('history.html')

@app.route('/settings/')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)