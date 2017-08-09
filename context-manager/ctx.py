from sqlite3 import connect


"""
with ctx() as x:
    pass

x = ctx().__enter__

try:
    pass
finally:
    x.__exit__()

"""

with connect("test.db") as conn:
    cur = conn.cursor()
    cur.execute("create table points(x int, y int)")
    cur.execute("insert into points(x, y) values(1, 2)")
    cur.execute("insert into points(x, y) values(1, 4)")
    cur.execute("insert into points(x, y) values(3, 2)")
    cur.execute("insert into points(x, y) values(5, 2)")
    for row in cur.execute("select x, y from points"):
        print(row)
    for row in cur.execute("select sum(x * y) from points"):
        print(row)
    cur.execute("drop table points")

