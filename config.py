#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "26148784"))
    API_HASH = os.environ.get("API_HASH", "e1428799c0aeccd0a3cd1f15606e7a80")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7148824590")
