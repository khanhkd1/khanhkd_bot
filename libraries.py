from flask import request
from config import VERIFY_TOKEN
import requests


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_user_id(data):
    return data['entry'][0]['messaging'][0]['sender']['id']


def get_api_data(url):
    r = requests.get(url)
    return r.json()['locations'][274]


def text_for_user(data):
    return f'Thông tin COVID ở Việt Nam:\n' \
           f'Số ca nhiễm: {data["latest"]["confirmed"]}\n' \
           f'Số ca tử vong: {data["latest"]["deaths"]}'
