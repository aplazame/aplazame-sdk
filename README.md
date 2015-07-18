# Aplazame Python Sdk

[![Build Status](https://img.shields.io/pypi/v/aplazame-sdk.svg)](https://pypi.python.org/pypi/aplazame-sdk) [![Downloads](https://img.shields.io/pypi/dm/aplazame-sdk.svg) ](https://pypi.python.org/pypi/aplazame-sdk) [![Drone](http://drone.aplazame.com/api/badge/github.com/aplazame/aplazame-sdk/status.svg?branch=master) ](http://drone.aplazame.com/github.com/aplazame/aplazame-sdk) [![Coveralls](https://coveralls.io/repos/aplazame/aplazame-sdk/badge.svg?branch=master&service=github) ](https://coveralls.io/github/aplazame/aplazame-sdk?branch=master) [![Aplazame](https://aplazame.com/static/img/banners/Banner-white-1.png "Aplazame") ](https://aplazame.com "Aplazame")

Aplazame, a consumer credit company, offers a payment system that can be used by online buyers to receive funding for their purchases.


### Installation

To install aplazame-sdk, simply:

```sh
$ pip install aplazame-sdk
```


### Usage

```python
>>> from aplazame_sdk import Client
>>> client = Client('->AccessToken<-', sandbox=True, version='1', ctype='json')
>>> r = client.orders(page=2)
>>> r.json()
{
  "cursor": {
    "after": 3,
    "before": 1
  },
  "paging": {
    "count": 314,
    "next": "https://api.aplazame.com/orders?page=3",
    "previous": "https://api.aplazame.com/orders?page=1"
  },
  "results": [
  ]
}
>>> r.status_code
200
```


#### Http

```http
GET /orders HTTP/1.1
Accept: application/vnd.aplazame.sandbox.v1+json
Authorization: Bearer ->AccessToken<-
Host: api.aplazame.com

HTTP/1.1 200 OK
Content-Type: application/vnd.aplazame.sandbox.v1+json
```

### Documentation

Documentation is available at [docs.aplazame.com](http://docs.aplazame.com).

