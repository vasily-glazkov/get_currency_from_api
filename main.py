import requests
from datetime import datetime
from flask import Flask


def get_currencies_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).json()
    currencies = list(data['Valute'].values())
    return currencies


app = Flask(__name__)


def create_html(currencies):
    date = datetime.now().date()
    date = date.strftime("%A, %-d %B %Y")
    text = f'<h1>Курс валют за {date}</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in currencies[0]:
        text += f'<th><th>'
    text += '</tr>'
    for currency in currencies:
        text += '<tr>'
        for v in currency.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    return text


@app.route("/")
def index():
    currencies = get_currencies_list()
    html = create_html(currencies)
    return html


if __name__ == "__main__":
    app.run()
