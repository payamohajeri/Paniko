#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append( "./instabot" )

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time

bot = InstaBot(login="username", password="password")
