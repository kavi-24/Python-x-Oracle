# import oracledb
# oracledb.init_oracle_client()

# username = "KAVI"
# password = "kavi_1203"
# host = "localhost"
# port = 1521
# service_name = "XE"

# dsn = f"{username}/{password}@{host}:{port}/{service_name}"
# connection = oracledb.connect(dsn=dsn)

# with connection.cursor() as cursor:
#     cursor.execute("""
#     create table MyPoints (
#         id number(9) not null,
#         point sdo_point_type not null
#         );""")
#     cursor.execute("""
#         insert into MyPoints values (1, sdo_point_type(125, 375, 0));
#         """)
#     cursor.execute("""
#         create or replace function spatial_queryfn (
#             a_Id     number
#         ) return sdo_point_type is
#         t_Result sdo_point_type;
#         begin
#             select point
#             into t_Result
#             from MyPoints
#             where Id = a_Id;
#         return t_Result;
#         end;"""
#     )

# obj_type = connection.gettype("SDO_POINT_TYPE")
# cursor = connection.cursor()
# return_val = cursor.callfunc("spatial_queryfn", obj_type, [1])
# print(f"({return_val.X}, {return_val.Y}, {return_val.Z})")
# # will print (125, 375, 0)

# connection.close()
