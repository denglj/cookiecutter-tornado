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

    def update_full(self, example_id):
        # full update specified resource through PUT method
        pass

    def update_collection_full(self):
        # full update resources through PUT method without arguments
        pass

    def update_partial(self, example_id):
        # partial update specified resource through PATCH method
        pass

    def update_collection_partial(self):
        # partial update resources through PATCH method without arguments
        pass

    def delete(self, example_id):
        # delete specified resource through DELETE method
        pass

    def delete_collection(self):
        # delete whole resources of this kind through DELETE method without arguments
        pass

    def http_options(self, example_id):
        allow_method = ['GET', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
        if example_id:
            allow_method.append('POST')
        self.set_status(204)
        self.set_header('Allow', ','.join(allow_method))
        self.finish()

    def header(self, example_id):
        # like GET , but only return http header
        # you should complete this function
        self.finish()
