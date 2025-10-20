import db


def test_mongo_db():
    mongo_db = db.MongoDB.from_uri("mongodb://localhost:27017/db")
    print(mongo_db.client)

    mongo_db = db.MongoDB(
        host="localhost",
        port=27017,
        username=None,
        password=None,
        dbname="db"
    )
    print(mongo_db.client)


if __name__ == '__main__':
    test_mongo_db()
