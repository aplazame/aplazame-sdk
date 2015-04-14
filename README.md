[ ![Image](https://aplazame.com/static/img/banners/Banner-white-1.png "Aplazame") ](https://aplazame.com "Aplazame")

# aplazame-sdk


## Install package
```
pip install git+https://github.com/calvinpy/aplazame-sdk.git
```

## Authentication
[Oauth2](http://en.wikipedia.org/wiki/OAuth) open standard for authorization.

The OAuth 2.0 Framework was published as [RFC 6749](http://tools.ietf.org/html/rfc6749)

OAuth2 is more simple to work with than OAuth1, and provides much better security.


## Request Headers
* Authorization: oauth2 Bearer Token published as [RFC 6750](http://tools.ietf.org/html/rfc6750)
* Accept: to specify certain media types which are acceptable for the response.

## API versioning
Although we currently allow for versioned URL, as for example `api.aplazame.com/v1/orders`, we consider it a better practice the use of the header `Accept` in the request to specify the type and format of the API service response.

Thus we allow the following types of header

* Accept: application/vnd.aplazame-v1+json
* Accept: application/vnd.aplazame-v1+jsonp
* Accept: application/vnd.aplazame-v1+xml
* Accept: application/vnd.aplazame-v1+yaml

If you do not specify any version by header or by URL, the latest version of the API will be activated. Since a new version of API can deprecate certain fields, this type of practice is nor recommended.

## Sanbox mode
Aplazame has a sandbox mode for your unit tests. If you want to make a request in sandbox mode, it must be specified in the `Accept` header just before the Api version.

**application/vnd.aplazame.sandbox-v1+json**

## Decimals
All amounts related to taxes, discounts and prices will be formatted as an integer including two decimals. For example, if an item has a price of *12.50* should be formatted as an integer *1250*.


## Usage
```python
from aplazame_sdk import Client

client = Client('YOUR-ACCESS-TOKEN', format_type='json')
response = client.orders()
```

## Pagination
```python
response = client.orders(page=2)
```


## Request example

```http
GET /orders HTTP/1.1
Accept: application/vnd.aplazame-v1+json
Authorization: Bearer <ACCESS_TOKEN>
Host: api.aplazame.com
```

```http
HTTP/1.1 200 OK
Content-Type: application/vnd.aplazame-v1+json

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
```

### For complete documentation for the API.

Full documentation for the API is available at [http://docs.aplazame.com/](http://docs.aplazame.com/).

For questions and support [soporte@aplazame.com](mailto:soporte@aplazame.com?subject=Hello world).

