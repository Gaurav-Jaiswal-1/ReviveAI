from models import get_response

def chatbot_reply(user_input, category):
    response = get_response(user_input, category)
    return response
