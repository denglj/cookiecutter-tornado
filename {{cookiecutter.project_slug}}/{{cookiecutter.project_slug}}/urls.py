#!/usr/bin/env python
# encoding: utf-8


from handlers import base


url_patterns = [
    (r"/", base.MainHandler),
]
