import requests

urlApi = "https://min-api.cryptocompare.com/data/histoday?fsym=${fromcur}&tsym=${tocur}&limit=2000&toTs{}"

def getCoinHistoryDay(fromcur, tocur, date):
    url = urlApi.replace("${fromcur}", fromcur)
    url = url.replace("${tocur}", tocur)
    url = url.format(date)

    r = requests.get(url)
    data = r.json()
    return data