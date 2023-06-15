import oracledb
oracledb.init_oracle_client()

username = "KAVI"
password = "kavi_1203"
host = "localhost"
port = 1521
service_name = "XE"

dsn = f"{username}/{password}@{host}:{port}/{service_name}"
connection = oracledb.connect(dsn=dsn)

cursor = connection.cursor()


def output_type_handler(cursor, name, default_type, size, precision, scale):

    def out_converter(d):
        if isinstance(d, str):
            return f"{d} was a string"
        else:
            return f"{d} was not a string"

    if default_type == oracledb.DB_TYPE_NUMBER:
        return cursor.var(oracledb.DB_TYPE_VARCHAR,
             arraysize=cursor.arraysize, outconverter=out_converter)

cursor.outputtypehandler = output_type_handler



for row in cursor.execute("select table_name from user_tables"):
    print(row)

cursor.execute("select * from customers")
while True:
    row = cursor.fetchone()
    # rows = cursor.fetchmany(size=num_rows)
    # rows = cursor.fetchall()
    if row is None:
        print("No more rows")
        break
    print(row)

cursor.execute("select * from customers")
for column in cursor.description:
    print(column)


'''
cursor = connection.cursor(scrollable=True)
cursor.execute("select * from ChildTable order by ChildId")

cursor.scroll(mode="last")
print("LAST ROW:", cursor.fetchone())

cursor.scroll(mode="first")
print("FIRST ROW:", cursor.fetchone())

cursor.scroll(8, mode="absolute")
print("ROW 8:", cursor.fetchone())

cursor.scroll(6)
print("SKIP 6 ROWS:", cursor.fetchone())

cursor.scroll(-4)
print("SKIP BACK 4 ROWS:", cursor.fetchone())
'''


cursor.close()
connection.close()
