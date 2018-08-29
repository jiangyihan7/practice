# -*- coding: utf-8 -*-
import requests,time
from _datetime import datetime

BITCOIN_API_URL= 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/c3ncS6_U7_r-8PTRGgdADc'


def get_latest_bitoin_price():
    response=requests.get(BITCOIN_API_URL)
    response_json=response.json()
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    data={'value1':value}
    ifttt_event_url=IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url,json=data)

#将bitcoin_history作为参数，然后使用被Telegram允许的基本HTML标签（像<br>, <b>, <i> 等等）变换格式
def format_bitcoin_history(bitcoin_history):
    rows=[]
    for bitcoin_price in bitcoin_history:
        date=bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price=bitcoin_price['price']
        row='{}:$<b>{}</b>'.format(date,price)
        rows.append(row)

    return '<br>'.join(rows)
BITCOIN_PRICE_THRESHOLD = 10000
def main():
    bitcoin_history=[]
    while True:
        price=get_latest_bitoin_price()
        date=datetime.now()
        bitcoin_history.append({'date':date,'price':price})
        #发送紧急通知
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)
        #一旦有五条更新，发送电报通知
        if len(bitcoin_history)==5:
            post_ifttt_webhook('bitcoin_price_update',format_bitcoin_history(bitcoin_history))
            #清空
            bitcoin_history=[]
        #至少5分钟才能得到新数据
        time.sleep(2*60)
if __name__ == '__main__':
    main()