#!/usr/bin/env python3
#
# Copyright (C) 2020 Dusan Mitrovic <dusan@dusanmitrovic.xyz>
# Licensed under the terms of the GNU GPL v3 only.
# 
# i3blocks script to check the number of unread messages in the mailbox
import imaplib
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

imap_username = os.getenv('IMAP_USERNAME')
imap_password = os.getenv('IMAP_PASSWORD')
imap_host = os.getenv('IMAP_HOST')
imap_port = os.getenv('IMAP_PORT')

imap = imaplib.IMAP4_SSL(imap_host, imap_port)
imap.login(imap_username, imap_password)
imap.select('INBOX')

status, response = imap.search(None, 'UNSEEN')

unread_messages_count = len(response[0].split())

print(unread_messages_count)

imap.logout()
