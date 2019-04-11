import os
import time

from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return f'root'


#   Cache


from werkzeug.contrib.cache import RedisCache
CACHE = RedisCache(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=1, default_timeout=300)


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


from tasks import generate_report, download_data


@app.route('/report/<input_param>')
def report(input_param):
    return generate_report.delay(input_param).id


@app.route('/data/<input_param>')
def data(input_param):
    return download_data.delay(input_param).id


import rq_dashboard
rq_settings = rq_dashboard.default_settings
rq_settings.REDIS_HOST=os.environ['REDIS_HOST']
app.config.from_object(rq_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")


#


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)