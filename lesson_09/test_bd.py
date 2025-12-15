from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:1234@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'users'


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    result_before = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    sql = text("""
        INSERT INTO subject("subject_title", "subject_id")
        VALUES (:title, :id)
    """)

    connection.execute(sql, {"title": "TOE", "id": "222"})
    transaction.commit()

    result_after = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    connection.close()
    assert result_after == result_before + 1

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql_update = text("""
    UPDATE subject
    SET subject_title = :subject_title
    WHERE subject_id = :id
""")
    result = connection.execute(sql_update, {"subject_title": 'New TOE', "id": 222})

    transaction.commit()
    result_select = connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": 222}
    ).fetchone()
    connection.close()
    assert result_select.subject_title == "New TOE"

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    result_before = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    sql = text("DELETE FROM subject WHERE subject_id = :id")
    connection.execute(sql, {"id": 222})

    transaction.commit()

    result_after = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    connection.close()

    assert result_after == result_before - 1
