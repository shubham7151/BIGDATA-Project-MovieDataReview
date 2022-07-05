from pyhive import hive

def connection_setup(host_var,port_var,username_var):    
    return hive.Connection(host=host_var,port=port_var,username=username_var)  

def create_cursor (connection):
    return connection.cursor()

def drop_table(cur, db_name ,table_name):
    try:
        cur.execute('drop table ' + db_name +'.'+table_name )
        print("table dropped successful")
    except Exception as e:
        print(e)