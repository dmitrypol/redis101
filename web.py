import os
import time

from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return f'root'


#   Cache


from werkzeug.contrib.cache import RedisCache
CACHE = RedisCache(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0, default_timeout=300)


@app.route('/nocache/<input_param>')
def nocache(input_param):
    return _slow_method(input_param)


@app.route('/cache/<input_param>')
def cache(input_param):
    key = 'slow_method_cache:' + input_param
    result = CACHE.get(key)
    if result is None:
        result = _slow_method(input_param)
        CACHE.set(key, result, timeout=60)
    return result + ' - from cache'


def _slow_method(input_param):
    #   query DB or external API
    time.sleep(5)
    return 'slow method results - ' + input_param


#   Background job queue


from redis import Redis
from rq import Queue
redis_conn = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=1)
RQ = Queue(connection=redis_conn)
from common import generate_report


@app.route('/request_report/<input_param>')
def request_report(input_param):
    job = RQ.enqueue(generate_report, input_param)
    return job.id


#


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)