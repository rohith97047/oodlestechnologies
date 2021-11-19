import time

import redis
from flask import flask


app = flask(__name__)
cache = redis.redis(host='redi', port=6379)


def get_hit_count():
    retries = 5
    while true:
        try:
            return cache.incr('hits')
        except redis.exceptions.connectionerror as exc:
            if retries == 0:
                raise exc
            retrie -=1
            time.sleep(0.5


@app.route('/')
def hello():
    count = get_hit_count()
    return 'hello world! I have been seen {} time.\n'.format(count)

if__name__=="__main__":
    app.run(host="0.0.0.", debug=true)
    
