import requests

url = "https://paper-api.alpaca.markets/v2/account"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "PK8PQEW3WJR8YYLX4A8I",
    "APCA-API-SECRET-KEY": "ewEMwsJOVJUgYZpPErTBSb6GppeDOIqyOwfWI4Zt"
}

response = requests.get(url, headers=headers)

print(response.text)





#Template to reating Buy/Sell feature

#from flask import Blueprint, render_template, requests
#
#pages = Blueprint('pages', __name__)
#
#@pages.route('/', methods=['GET', 'POST'])
#def index():
#
#    if request.method == 'POST':
#        oredertype = request.form.get('ordedrtype')
#        ticker= request.form.get('ticker')
#        quantity = request.form.get('quantity')
#        print(ordertype)
#        print(ticker)
#        print(quantity)
#
#        return render_templates('index.html')