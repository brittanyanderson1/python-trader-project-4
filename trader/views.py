from django.shortcuts import render


#trading_client = TradingClient("PK8PQEW3WJR8YYLX4A8I", "ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt")

        #symbol_or_symbols = "AAPL",
        #start=datetime(2024, 1, 30, 14, 30),
        #end=datetime(2024, 1, 30, 14, 45)
#)

#trades = data_client.get_trades(request_params)

#print(trades)
#print(trading_client.get_account().account_number)
#print(trading_client.get_account().buying_power)




def home(request):
        #from alpaca.trading.client import TradingClient
        #trading_client = TradingClient("PK8PQEW3WJR8YYLX4A8I", "ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt")
        #data_client = StockHistoricalDataClient("PK8PQEW3WJR8YYLX4A8I", "ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt")
        #from alpaca.data import StockHistoricalDataClient, StockTradesRequest
        #from datetime import datetime
        #import requests
        #import json
        #url = "https://data.alpaca.markets/v2/stocks/bars?symbols=AAPL&timeframe=1Day&start=2024-01-02&end=2024-01-05&limit=1000&adjustment=raw&feed=sip&currency=USD&sort=asc"

        #headers = {
        #"accept": "application/json",
        #"APCA-API-KEY-ID": "PK8PQEW3WJR8YYLX4A8I",
        #"APCA-API-SECRET-KEY": "ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt"
        #}

        #requests.get(url, headers=headers)

        return render(request, 'home.html', {})
              
def about(request):
        return render(request, 'about.html', {})

#       API Keys
#   api_request = requests.get("https://data.alpaca.markets/v2/stocks/bar")
#   Endpoint
#   https://paper-api.alpaca.markets/v2
#   Key
#   PK8PQEW3WJR8YYLX4A8I
#   Secret
#   ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt
#   Note: Your secret key will disappear after refreshing or navigating away from this page.


    #The Base URL for the historical endpoints is:  https://data.alpaca.markets/{version}   https://data.alpaca.markets/v2/stocks/bar   


    #Steps to use the stream
    #To establish a connection use the stream URL depending on the data you'd like to consume. The general schema of the URL is:    wss://stream.data.alpaca.markets/{version}/{feed}
    
    #Upon successfully connecting, you will receive the welcome message:    [{"T":"success","msg":"connected"}]

    #Authenticate with HTTP headers
    #You can set the same headers used for the historical market data and trading endpoints:    APCA-API-KEY-ID and APCA-API-SECRET-KEY

    #Here's an example using a WebSocket client called websocat:    $ websocat wss://stream.data.alpaca.markets/v2/test \
                                                                    #-H="APCA-API-KEY-ID: {KEY_ID}" -H="APCA-API-SECRET-KEY: {SECRET}"

#You can send one or more subscription messages. The general format of the subscribe message is this:
#   JSON

#   {
#     "action": "subscribe",
#     "channel1": ["SYMBOL1"],
#     "channel2": ["SYMBOL2","SYMBOL3"],
#     "channel3": ["*"]
#   }

#   You can subscribe to a particular symbol or to every symbol using the * wildcard.
#   For example in the test stream, you can send this message:
#   JSON
#   {"action":"subscribe","trades":["FAKEPACA"]}