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

'''
If a procedure with the following definition exists:

create or replace procedure myproc (
    a_Value1                            number,
    a_Value2                            out number
) as
begin
    a_Value2 := a_Value1 * 2;
end;
'''

with connection.cursor() as cursor:
    cursor.execute("""
            create or replace procedure myproc (
                a_Value1 number,
                a_Value2 out number
            ) as
            begin
                a_Value2 := a_Value1 * 2;
            end;"""
    )
    cursor.execute("""
            select line, position, text
            from user_errors
            where name = 'BADPROC' and type = 'PROCEDURE'
            order by name, type, line, position""")
    errors = cursor.fetchall()
    if errors:
        for info in errors:
            print("Error at line {} position {}:\n{}".format(*info))
    else:
        print("Created successfully")

    out_val = cursor.var(int)
    cursor.callproc('myproc', [123, out_val])
    print(out_val.getvalue())        # will print 246

with connection.cursor() as cursor:
    cursor.execute(
        """
        create or replace function myfunc (
            a_StrVal varchar2,
            a_NumVal number
        ) return number as
        begin
            return length(a_StrVal) + a_NumVal * 2;
        end;
        """
    )
    return_val = cursor.callfunc("myfunc", int, ["a string", 15])
    print(return_val)        # will print 38

connection.close()
