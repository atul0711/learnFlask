from sqlalchemy import create_engine, text, select

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
# engine = create_engine("sqlite:////api_project/chinook.db", echo=True)


with engine.connect() as conn:
    conn.execute(text("create table employees (a text, b text)"))

# "commit as you go"
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    rows = conn.execute(text("select * from some_table"))
    for row in rows:
        print(row)
