import os

from redis import Redis
from rq import Worker, Queue

redis_conn = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
queue = Queue('default', connection=redis_conn)
WORKER = Worker([queue], connection=redis_conn)


if __name__ == '__main__':
    WORKER.work()
