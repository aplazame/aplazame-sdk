[ ![Image](https://aplazame.com/static/img/banners/Banner-white-1.png "Aplazame") ](https://aplazame.com "Aplazame")

# aplazame-sdk

## Install package
```
pip install git+https://github.com/aplazame/aplazame-sdk.git
```

## Usage
```python
from aplazame_sdk import Client

client = Client('YOUR-ACCESS-TOKEN', format_type='json')
response = client.orders()
```

### Pagination
```python
response = client.orders(page=2)
```


### Request example

```http
GET /orders HTTP/1.1
Accept: application/vnd.aplazame.v1+json
Authorization: Bearer ->AccessToken<-
Host: api.aplazame.com
```

```http
HTTP/1.1 200 OK
Content-Type: application/vnd.aplazame.v1+json

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

## Documentation & Support

Full documentation for the API is available at [http://docs.aplazame.com/](http://docs.aplazame.com/).

For questions and support [soporte@aplazame.com](mailto:soporte@aplazame.com?subject=Hello world).

