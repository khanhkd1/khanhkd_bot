from flask import Flask, request
from config import ACCESS_TOKEN, URL_COVID_DATA
from libraries import verify_fb_token, get_user_id, get_api_data, text_for_user
from pymessenger4 import Bot

app = Flask(__name__)
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        bot.send_text_message(get_user_id(output), 'text')
        # bot.send_text_message(get_user_id(output), text_for_user(get_api_data(URL_COVID_DATA)))
    return "Message Processed"


if __name__ == "__main__":
    app.run(debug=True)
