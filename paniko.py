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

links=open('./links', 'w+')

bot = InstaBot(login="", password="")
bot.get_media_id_recent_feed()
for feed in bot.media_on_feed:
    links.write(feed["display_src"] + "\n")

exit()
