import schedule
import requests


def greeting():
    """Greeting function"""

    todos_dict = {
        '06:00': 'get up',
    }

    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"

    print(btc_price)

if __name__ == '__main__':
    schedule.every(9).seconds.do(greeting)
    # schedule.every(5).minutes.do(greeting)
    # schedule.every().hour.do(greeting)
    # schedule.every().day.at('21:51').do(greeting)
    # schedule.every().thursday.do(greeting)
    # schedule.every().friday.at('23:45').do(greeting)
    while True:
        schedule.run_pending()