#!/usr/bin/env python
# encoding: utf-8

import os.path

from tornado.options import define

define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")

settings = {
    "debug": True,
    "cookie_secret": "!!CHANGEME!!",
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "xsrf_cookies": False
}
