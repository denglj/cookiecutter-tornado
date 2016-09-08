#!/usr/bin/env python
# encoding: utf-8

from {{cookiecutter.project_slug}}.common import RESTfulHandler


class Example(RESTfulHandler):

    def gets(self, example_id):
        self.finish({"example_id": example_id,
                     "discription": "you had query an example resource."})

    def lists(self):
        self.finish("through GET method, you can get all resources by access the api without any argument.")

    def create(self):
        self.finish({'method': 'create',
                     'discription': 'create resource with given arguments',
                     'arguments': self.request.arguments})

    def update(self, example_id):
        # update specified resource through PUT method
        pass

    def update_collection(self):
        # update whole resources through PUT method without arguments
        pass

    def delete(self, example_id):
        # delete specified resource through DELETE method
        pass

    def delete_collection(self):
        # delete whole resources of this kind through DELETE method without arguments
        pass
