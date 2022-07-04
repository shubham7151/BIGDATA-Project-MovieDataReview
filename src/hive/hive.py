from pyhive import hive

def connection_setup(host_var,port_var,username_var):    
    return hive.Connection(host=host_var,port=port_var,username=username_var)  

def create_cursor (connection):
    return connection.cursor()
