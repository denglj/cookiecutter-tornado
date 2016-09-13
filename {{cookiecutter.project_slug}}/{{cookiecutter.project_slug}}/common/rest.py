#!/usr/bin/env python
# encoding: utf-8

import tornado.web
from tornado.escape import json_encode


class RESTfulHandler(tornado.web.RequestHandler):

    methods = ("lists", "gets", "create", "header", "http_options"
               "update_full", "update_collection_full",
               "update_partial", "update_collection_partial",
               "delete", "delete_collection")

    def __init__(self, application, request, **kwargs):
        super(RESTfulHandler, self).__init__(application, request, **kwargs)
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def __getattr__(self, name):
        if name in self.methods and self.request.headers:
            raise tornado.web.HTTPError(500)
        else:
            raise AttributeError

    def get(self, resource_id=None):
        if resource_id is None:
            return self.lists()
        else:
            return self.gets(resource_id)

    def post(self, resource_id=None):
        if resource_id is None:
            return self.create()
        else:
            raise tornado.web.HTTPError(500)

    def put(self, resource_id=None):
        if resource_id is None:
            return self.update_collection_full()
        else:
            return self.update_full(resource_id)

    def patch(self, resource_id=None):
        if resource_id is None:
            return self.update_collection_partial()
        else:
            return self.update_partial(resource_id)

    def delete(self, resource_id=None):
        if resource_id is None:
            return self.delete_collection()
        else:
            return self.delete(resource_id)

    def options(self, resource_id=None):
        return self.http_options(resource_id)

    def head(self, resource_id=None):
        return self.header(resource_id)

    def finish(self, chunk=None):
        if chunk is not None:
            chunk = json_encode(chunk)
        super(RESTfulHandler, self).finish(chunk)
