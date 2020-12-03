from flask import Flask

from flask import jsonify
from flask import Blueprint
import requests

from api.jobs_api import jobs_api
from api.skills_api import skills_api
from dal.models import db
from dal.load_data import load_data_from_externalapi
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///openskill.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify("API for Openskill database")

app.register_blueprint(jobs_api)
app.register_blueprint(skills_api)    

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    load_data_from_externalapi()
    app.run(debug=True)








