import csv

import redis

REDIS_COUNT = redis.Redis(db=2).pipeline()
REDIS_ZSET = redis.Redis(db=3)


def redis_count(ip):
    REDIS_COUNT.incr(ip)
    REDIS_COUNT.expire(ip, 3600 * 24)
    REDIS_COUNT.execute()


def redis_zset(ip):
    REDIS_ZSET.zincrby('ips', 1, ip)


with open('tmp/data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        ip = row[0]
        redis_count(ip)
        redis_zset(ip)