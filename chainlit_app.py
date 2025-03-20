import chainlit as cl
from models import get_response

@cl.on_message
async def main(message):
    user_input = message.content
    category = "fitness"  # You can add buttons to select category
    response = get_response(user_input, category)
    await cl.Message(response).send()
