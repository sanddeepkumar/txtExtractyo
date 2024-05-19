#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7174606656:AAES4xrsYwn9gi8O9knJBM0wwC2NihyGKTw")
    API_ID = int(os.environ.get("API_ID", "23634056"))
    API_HASH = os.environ.get("API_HASH", "f2debf49c2f57bad88086ecd17cb5df3")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5082207960")
