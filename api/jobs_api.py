from flask import Blueprint
from service import jobs_service 
from flask import request, jsonify

jobs_api = Blueprint('jobs_api', __name__)


@jobs_api.route('/api/jobs/all', methods=['GET'])
def get_job_all():
    results = jobs_service.get_all_jobs()
    return jsonify(results)


@jobs_api.route('/api/jobs', methods=['GET'])
def get_job():
    results = jobs_service.get_job(request)
    return jsonify(results)










