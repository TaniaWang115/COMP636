import connect, mysql.connector


connection = None
dbconn = None


def DBConnect():
    global dbconn
    global connection
    if dbconn == None:
        connection = mysql.connector.connect(user=connect.dbuser, \
        password=connect.dbpass, host=connect.dbhost, \
        database=connect.dbname, autocommit=True)
        dbconn = connection.cursor()
        return dbconn
    else:
        return dbconn


def DBOperator(sqlCommands):    
    cur = DBConnect()
    cur.execute(sqlCommands)
    select_result = cur.fetchall()
    return select_result

def DBOperatorFetchOne(sqlCommands):
    cur = DBConnect()
    cur.execute(sqlCommands)
    select_result = cur.fetchone()
    return select_result