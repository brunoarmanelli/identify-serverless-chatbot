#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Plugins/Modules
import logging
import telebot
import os

# Bot Env
env = os.environ['AZURE_FUNCTIONS_ENVIRONMENT']

# Set Logger
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# Init Chatbot
bot = telebot.TeleBot(os.environ['TelegramBotKey'])

# Message Handlers
from .handlers import commands, media, plain

