from app import app, mysql

def query_data(sql, parameter_list):
    data = {}
    cursor = mysql.connection.cursor()
    
    if len(parameter_list)>0:
        cursor.execute(sql, parameter_list)
    else:
        cursor.execute(sql)

    data = cursor.fetchall()
    cursor.close()
     
    return data

def store_data(sql, parameter_list):
    cursor = mysql.connection.cursor()
    if parameter_list:
        cursor.execute(sql, parameter_list)
    else:
        cursor.execute(sql)

    cursor.connection.commit()
    cursor.close()

def insert_many(sql, parameter_list):
    cursor = mysql.connection.cursor()
    # parameter list format
    # [(a,b), (c,d)]
    cursor.executemany(sql, parameter_list)
    cursor.connection.commit()
    cursor.close()

# check if the paramter list is safe
def isSafeParameterList(param_list):
    pass