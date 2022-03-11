from cgitb import handler
from statistics import mode
import discord
import logging

class Logger:
    
    @classmethod
    def start(cls):
        logger = logging.getLogger('discord')
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.log', mode='w', encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)