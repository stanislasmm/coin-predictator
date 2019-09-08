from connector.cryptocompare import getCoinHistoryDay
from services.DataDb import create_mysql_connexion, insert_data

fromcur = "BTC"
tocur = "USD"

conn = create_mysql_connexion()
datas = getCoinHistoryDay(fromcur, tocur, "1546300800")

print(datas)
insert_data(conn, datas["Data"], fromcur, tocur)