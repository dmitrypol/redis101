## Using the app

```
docker-compose up --build -d --scale worker=2

python dataproc.py

docker logs -f redis101_worker_1

docker logs -f redis101_worker_2
```

* http://localhost:5001/cache/foo
* http://localhost:5002/nocache/foo
* http://localhost:5001/report/1
* http://localhost:5001/data/2
* http://localhost:5001/rq/

## Usefull links

* https://redis.io/
* http://flask.pocoo.org/
* http://flask.pocoo.org/docs/1.0/patterns/caching/
* https://github.com/andymccurdy/redis-py
* http://python-rq.org/
* https://github.com/eoranged/rq-dashboard
* https://github.com/rq/Flask-RQ2
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs
* https://realpython.com/flask-by-example-implementing-a-redis-task-queue/
* https://testdriven.io/blog/asynchronous-tasks-with-flask-and-redis-queue/
* https://www.fullstackpython.com/redis.html