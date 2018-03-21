#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging


logger = logging.getLogger(__name__)


def media_id_to_code(media_id):
    """
    Converts media_id of an Instagram post to code that used in URL.
    :param media_id: id of the post
    :return: code that used in Instagram URL
    """
    logger.info("Converting media_id %s to code", media_id)
    media_id = int(media_id.split("_")[0])
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    short_code = ''
    while media_id > 0:
        remainder = media_id % 64
        media_id = media_id // 64
        short_code = alphabet[int(remainder)] + short_code
    return short_code


def code_to_media_id(short_code):
    """
    Converts code of an Instagram post to id.
    :param short_code: code that used in Instagram URL
    :return: id of the post
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
    media_id = 0
    for letter in short_code:
        media_id = (media_id*64) + alphabet.index(letter)
    return media_id


def username_to_id(username):
    """
    Converts username of an Instagram account to the ID.
    :param username: Instagram account username
    :return: Instagram account ID
    """
    logger.info('Converting username \'%s\' to ID', username)
    url = 'https://www.instagram.com/{}/?__a=1'.format(username)
    r = requests.get(url)
    json = r.json()
    return json['graphql']['user']['id']
