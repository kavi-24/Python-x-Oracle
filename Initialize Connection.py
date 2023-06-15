import oracledb
oracledb.init_oracle_client()

username = "KAVI"
password = "kavi_1203"
host = "localhost"
port = 1521
service_name = "XE"

dsn = f"{username}/{password}@{host}:{port}/{service_name}"
connection = oracledb.connect(dsn=dsn)

# connection = oracledb.connect(user="hr", password=userpwd, dsn="localhost/orclpdb")
print(connection.version)
print(connection.dsn)
print(connection.username)
print(connection.autocommit)

connection.close()