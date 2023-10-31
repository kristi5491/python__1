# -*- coding: utf-8 -*-

import random

answers = ['yes', 'no', 'maybe']

def charivna_kulka(question):
    """
    Ця функція приймає запитання як вхідні дані і повертає випадкову відповідь.

    :param pytannia: Питання, яке ви бажаєте задати чарівному кульцю.
    :type pytannia: str

    :return: Випадкова відповідь ('так', 'ні' або 'можливо').
    :rtype: str
    """
    random_choice = random.choice(answers)
    if not question:
        return 'You didnt ask question'
    elif type(question) is not str:
        return 'invalid input'
    return random_choice



