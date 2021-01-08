import os
import mysql.connector
from datetime import datetime, date

host = os.environ["MYSQL_HOST"]
port = int(os.environ["MYSQL_PORT"])
print("host: " + str(host) + " | port: " + str(port))


TABLE_QUERY = (
    "CREATE TABLE `messages` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `user` varchar(60) NOT NULL,"
    "  `channel` varchar(60) NOT NULL,"
    "  `text` VARCHAR(255) NOT NULL,"
    "  `ts` date NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB") 

INSERT_QUERY = ("INSERT INTO messages "
               "(user, channel, text, ts) "
               "VALUES (%s, %s, %s, %s)")


def get_query(q):
    
    cnx = mysql.connector.connect(host = host, port = port, user="root", password="password", database="db")
    # falta comprobacion, querys soportadas !!!
    cur = cnx.cursor()
    try:
        cur.execute(q)
        n_fields = len(cur.description)
        fields_names = [i[0] for i in cur.description] 
        data = cur.fetchall()
        cnx.close()
        return fields_names, data
    except:
        return ["Error from query"], [("-")]


def save_msg(obj):
    
    if not checkTableExists(cnx, "messages"):
        cur = cnx.cursor()
        try:
            print("Creating table {}: ".format("MESSAGES"), end='')
            cur.execute(TABLE_QUERY)
        except mysql.connector.Error as err:
            print(err.msg)
        cur.close()
    
    cur = cnx.cursor()
    
    d_format = datetime.fromtimestamp(float(obj["ts"])).date()
    obj["ts"] = d_format
    
    cur.execute(INSERT_QUERY, list(obj.values()))
    
    res = ""

    if cur.lastrowid:
        res = "last insert id " + str(cur.lastrowid)
    else:
        res = "last insert id not found"

    cnx.commit()
    cur.close()    

    return res


def checkTableExists(cnx, tablename):
    dbcur = cnx.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    return False

