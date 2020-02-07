import requests
import time
import json
import datetime

msgUpd = 0

def makeReq(type = 'upd'):
    apiKey = '927609870:AAG7RDg2HG5zB_xhzzOsSDKVnPwbqHSXQdE'
    link2Docs = 'https://core.telegram.org/bots/api'
    baseUrl = f'https://api.telegram.org/bot{apiKey}/'
    sendMethod = 'sendMessage'
    updMethod = 'getUpdates'
    username = '@so2niko'
    chatId = 194287825
    groupId = -353351825
    if type == 'upd':
        r = requests.get(f'{baseUrl}{updMethod}')
    else:
        text = input('Enter a text')
        r = requests.get(f'{baseUrl}{sendMethod}?chat_id={groupId}&text={text}')

    # print(r.text)
    global msgUpd
    answ = json.loads(r.text)
    for i in answ['result']:
        #print(type(i['message']))
        if 'text' in i['message'] and msgUpd < i['update_id']:
            msgUpd = i['update_id']
            #{datetime.datetime.strptime(time.ctime(i['message']['date']), '%f')}
            str = f"{datetime.datetime.strptime( i['message']['date'], '%f')} :  {i['message']['from']['first_name']} : {i['message']['text']}"
            print(str)


while True:
    time.sleep(5)
    makeReq()

