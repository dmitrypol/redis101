import os
import time

from redis import Redis
redis_conn = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
from rq.decorators import job


@job('default', connection=redis_conn)
def generate_report(input_param):
    time.sleep(5)
    return {'input_param': input_param}


@job('default', connection=redis_conn)
def download_data(input_param):
    time.sleep(5)
    return {'download_data': input_param}    