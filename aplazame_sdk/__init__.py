#!/usr/bin/env python
#
# Copyright 2015-2016 calvin
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

__version__ = '0.1.0'

import json
import requests


class AplazameError(Exception):

    """
    Exception Handling
    """

    def __init__(self, response=None, format_type='json'):
        self.response = response
        self.code = response.status_code

        if format_type == 'json':
            try:
                error = json.loads(self.response.content)['error']
            except ValueError:
                pass
            else:
                self.message = error['message']
                self.type = error['type']

    def __str__(self):
        return "{self.code}.{self.message}".format(self=self)

    def __repr__(self):
        return str(self)


class Client(object):

    """
    A client for the Aplazame Recovery API.

    See http://docs.aplazame.apiary.io/
    for complete documentation for the API.
    """

    user_agent = 'AplazameSdk/rest-sdk-aplazame 0.1'

    def __init__(
            self, access_token, sandbox=False, version='1', format_type='json'):

        self.access_token = access_token
        self.version = version
        self.format_type = format_type
        self.sandbox = sandbox

    def endpoint(self, action):
        return "https://api.aplazame.com/{action}".format(action=action)

    @property
    def headers(self):
        if self.sandbox:
            site = 'aplazame.sandbox'
        else:
            site = 'aplazame'

        return {
            'User-Agent': self.user_agent,
            'Authorization': 'Bearer ' + self.access_token,
            'Accept': "application/vnd.{site}-v"
            "{self.version}+{self.format_type}".format(site=site, self=self)
        }

    def request(self, url, method, headers=None, **kwargs):
        http_headers = self.headers
        http_headers.update(headers or {})

        response = requests.request(
            method, url, headers=http_headers, **kwargs)

        if not (200 <= response.status_code < 300):
            raise AplazameError(response)

        if self.format_type == 'json':
            ret = json.loads(response.content)
        else:
            ret = response.content

        return ret

    def get(self, action, params=None, headers=None):
        return self.request(self.endpoint(
            action), 'GET', params=params, headers=headers)

    def page(self, action, page, rpp):
        params = {'page': page}

        if rpp is not None:
            params['rpp'] = rpp

        return self.get(action, params=params)

    def post(self, action, data=None, headers=None):
        return self.request(self.endpoint(
            action), 'POST', data=data, headers=headers)

    def put(self, action, data=None, headers=None):
        return self.request(self.endpoint(
            action), 'PUT', data=data, headers=headers)

    def delete(self, action, params=None, headers=None):
        return self.request(self.endpoint(
            action), 'DELETE', params=params, headers=headers)

    def merchants(self, page=None, rpp=None):
        if page is not None:
            return self.page('merchants', page, rpp)
        return self.get('merchants')

    def merchant_detail(self, id):
        return self.get("merchants/{id}".format(id=id))

    def customers(self, page=None, rpp=None):
        if page is not None:
            return self.page('customers', page, rpp)
        return self.get('customers')

    def customer_detail(self, id):
        return self.get("customers/{id}".format(id=id))

    def orders(self, page=None, rpp=None):
        if page is not None:
            return self.page('orders', page, rpp)
        return self.get('orders')

    def order_detail(self, id):
        return self.get("orders/{id}".format(id=id))
