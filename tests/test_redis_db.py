import db


def test_redis_db():
    redis_db = db.RedisDB.from_uri("redis://:@localhost:6379/0?encoding=utf-8&decode_responses=True")
    print(redis_db.redis)

    redis_db = db.RedisDB(
        host="localhost",
        port=6379,
        password=None,
        dbname=0
    )
    print(redis_db.redis)


if __name__ == '__main__':
    test_redis_db()
