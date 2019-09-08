import psycopg2

from datetime import datetime

def create_mysql_connexion():
    conn_str = "host=coin_predictator_postgres dbname=coin_predictator user=postgres password="
    try:
      return psycopg2.connect(conn_str)
    except:
        print("unable to connect to databse")

def insert_data(conn, data, fromcur, tocur):
    cursor = conn.cursor()
    for res in data:
      date = datetime.fromtimestamp(res["time"])
      cursor.execute("INSERT INTO prices (time, close, open, high, low, volumefrom, volumeto, pairfrom, pairto) VALUES"
                   "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (date, res["close"], res["open"], res["high"], res["low"], res["volumeto"], 0, fromcur, tocur))
      conn.commit()

    cursor.close()
    conn.close()