# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 05:40:26 2016

http://www.jwfrankfurt.tumblr.com/
@author: Jordan

I wrote this script to turn all the links to posts on my blog into
bitlinks and give me data on the number of times each link has been clicked.
It will likely not work on many (any?) other blogs.
This is just a fun script for my own use.

The only argument necessary to make this work with any other Bitly account
is a new access token. I've removed mine.

"""

import requests
import re
from bs4 import BeautifulSoup
import time


class YoungWarthog:
    def __init__(self, accessToken=None, blogLinks=None,
                 bitLinks=None, blogAddress=None):
        self.accessToken = accessToken
        self.blogLinks = blogLinks if blogLinks is not None else []
        self.bitLinks = bitLinks if bitLinks is not None else []
        self.blogAddress = blogAddress if blogAddress is not None else "http://www.jwfrankfurt.tumblr.com/"
        self.ssl_endpoint = "https://api-ssl.bitly.com/v3/user/"
        self._test()

    def getNewPosts(self):
        response = requests.get(self.blogAddress)
        soup = BeautifulSoup(response.text, "lxml")
        pages = soup.find("span", class_="pagination__stats").text
        n = re.compile(r"\d+")
        m = n.findall(pages)

        page = int(m[0])
        while (page <= int(m[1])):
            pagestring = str(page)
            response = requests.get(self.blogAddress + 'page/' + pagestring)
            soup = BeautifulSoup(response.text, "lxml")
            x = soup.find_all("a", class_="post__date")
            for link in x:
                longUrl = link.get("href")
                if (longUrl not in self.blogLinks):
                    self.blogLinks.insert(0, longUrl)
            page += 1
            time.sleep(0.15)
        return self.blogLinks

    def shorten(self, blogLinks=None):
        self.blogLinks = blogLinks if blogLinks is not None else self.blogLinks
        prepend = "YoungW"
        url = self.ssl_endpoint + 'link_save'

        for x, link in enumerate(self.blogLinks):
            p = {
                'access_token': self.accessToken,
                'longUrl': self.blogLinks[x],
                'title': prepend + self.blogLinks[x][35:47]
                }
            response = requests.get(url, params=p).json()
            self.bitLinks.append(response['data']['link_save']['link'])
        return self.bitLinks

    def clicks(self, unit=None, units=None,
               timezone=None, limit=None):
        unit = unit if unit is not None else 'day'
        units = units if units is not None else '-1'
        timezone = timezone if timezone is not None else 'America/New_York'
        limit = limit if limit is not None else '100'

        rollup = 'true'

        url = self.ssl_endpoint + 'clicks'
        p = {
            'access_token': self.accessToken,
            'unit': unit,
            'units': units,
            'timezone': timezone,
            'rollup': rollup,
            'limit': limit
            }
        response = requests.get(url, params=p).json()
        clickData = response['data']['user_clicks']
        return clickData

    def linkHistory(self, created_before=None, created_after=None,
                    limit=None, private=None):
        created_before = created_before if created_before is not None else ''
        created_after = created_after if created_after is not None else ''
        limit = limit if limit is not None else ''
        private = private if private is not None else ''

        url = self.ssl_endpoint + 'link_history'
        p = {
            'access_token': self.accessToken,
            'created_before': created_before,
            'created_after': created_after,
            'limit': limit,
            'private': private
            }
        response = requests.get(url, params=p).json()
        linkHistory = response['data']['link_history']
        return linkHistory

    def _test(self):
        if (self.accessToken is None):
            raise Exception("You must provide an access token")
        else:
            assert isinstance(self.accessToken, str)
