#!/bin/python
import logging
import os

from flask import Flask, jsonify, request
import datetime as dt
from service.alignmentservice import AlignmentService
from validator.alignmentvalidator import AlignmentValidator
from utilities.alignmentutils import AlignmentUtils
from logging.config import dictConfig

alignapp = Flask(__name__)
context_path = os.environ.get('SA_CONTEXT_PATH', '/sentence-alignment')


# REST endpoint to align files
@alignapp.route(context_path + '/alignment/align/async', methods=["POST"])
def createalignmentjob():
    service = AlignmentService()
    util = AlignmentUtils()
    validator = AlignmentValidator()
    data = request.get_json()
    error = validator.validate_input(data)
    if error is not None:
        return error
    return service.register_job(data)


# REST endpoint to fetch job status
@alignapp.route(context_path + '/alignment/jobs/get/<job_id>', methods=["GET"])
def searchjobs(job_id):
    service = AlignmentService()
    response = service.search_jobs(job_id)
    return jsonify(response)

# Health endpoint
@alignapp.route('/health', methods=["GET"])
def health():
    response = {"code": "200", "status": "ACTIVE"}
    return jsonify(response)

# Log config
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(threadName)s %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'info': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': 'info.log'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        'file': {
            'level': 'DEBUG',
            'handlers': ['info', 'console'],
            'propagate': ''
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['info', 'console']
    }
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
