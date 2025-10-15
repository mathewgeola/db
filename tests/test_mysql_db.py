import db


def test_mysql_db():
    mysql_db1 = db.MysqlDB.from_uri("mysql+pymysql://root:root@127.0.0.1:3306/db?charset=utf8mb4")
    mysql_db2 = db.MysqlDB(
        host="localhost",
        port=3306,
        username="root",
        password="root",
        dbname="db",
        charset="utf8mb4"
    )
    print(mysql_db1.connection)
    print(mysql_db2.connection)


if __name__ == '__main__':
    test_mysql_db()
