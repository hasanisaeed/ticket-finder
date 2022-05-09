import requests

import env


def send_email(message, subject="بلیط قطار"):
    return requests.post(env.MAIL_URL,
                         auth=("api", env.MAIL_KEY),
                         data={"from": env.MAIL_FROM,
                               "to": env.MAIL_TO,
                               "subject": subject,
                               'html': message
                               })


def dict2html(data):
    html = ''.join("<th style='font-weight: bold;'>" + x + "</th>"
                   for x in data[0].keys())
    for item in data:
        html += "<tr style='background-color: gray; color: white;'>" + \
                ''.join("<td>" + str(x) + "</td>" for x in item.values()) + "</tr>"
    return "<table style='text-align:center'>" + html + "</table>"
