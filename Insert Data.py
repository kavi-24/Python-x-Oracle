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


cursor.execute("insert into customers values (:customer_id, :customer_name, :city)", [1, "Fredico", None])
print("Rows inserted:", cursor.rowcount)

cursor.execute("""insert into customers (customer_name, city, customer_id) values (:2, :3, :1)""", ["Roger", "London", 2])

for row in cursor.execute("select * from customers"):
    print(row)

cursor.close()
connection.close()