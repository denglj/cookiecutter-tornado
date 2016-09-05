#!/usr/bin/env python
# encoding: utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload
from tornado.options import options

from settings import settings
from {{ cookiecutter.project_slug }}.urls import url_patterns


class MainApplication(tornado.web.Application):

    def __init__(self):
        super(MainApplication, self).__init__(self, url_patterns, **settings)


def main():
    app = MainApplication()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
