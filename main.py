import random
import requests
url = "https://api.telegram.org/bot1473432422:AAG-XeibvZUHIPhmm_8ZMVvch034H9qRMTg/"


# function that gets the chat id
def get_chat_id(chat_result):
    chat_id = chat_result['message']["chat"]["id"]
    return chat_id


# function that get message
def get_message_text(chat_result):
    message_text = chat_result['message']['text']
    return message_text


# function that get the most update chat
def most_updated(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    len_chat = len(result)-1
    return result[len_chat]


# function that sends message from bot
def send_message(chat_id, message_text):
    response = requests.post(url + 'sendMessage?chat_id='+str(chat_id)+'&text='+message_text)
    return response


def main():
    update_id = most_updated(url)["update_id"]
    while True:
        updated = most_updated(url)
        if update_id == updated["update_id"]:
            if get_message_text(updated).lower() == 'hi' or get_message_text(updated).lower() == 'hello':
                send_message(get_chat_id(updated), 'Hello my name is Dave, Type play to roll the dice')
            elif get_message_text(updated).lower() == "play":
                num1 = random.randint(1, 6)
                send_message(get_chat_id(updated), 'You have rolled the number ' + str(num1))
                send_message(get_chat_id(updated), 'To play again please enter play')

            else:
                send_message(get_chat_id(updated), 'Sorry, I didn\'t understand you')
            update_id += 1


main()
