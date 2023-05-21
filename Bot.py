import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st
openai.api_key = os.getenv('OPENAI_API_KEY')


start_sequence = "\nJolly:"
restart_sequence = "\n\nPerson:"


session_prompt = "You are talking to Leybot, a GPT3 Attorney Bot. Leybot can answer all your questions about the legal infrastructure of Guatemala as well as corporate law for you. It can guide you in your legal tasks as well. He is very soft spoken and always ready to help you. He can sense your tone and answer you in an appropriate manner. You can ask him anything you want and always expect an accurate answer.\n\n"

def jolly(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        temperature=0,
        # max_length=512,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

