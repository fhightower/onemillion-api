# onemillion API

View it at [onemillion.hightower.space](http://onemillion.hightower.space).

API/UI Interface to check if a domain is in a top million domain lists from Alexa or Cisco. This project is built on the [onemillion](https://github.com/fhightower/onemillion) python package.

## Using the UI

Visit [onemillion.hightower.space](http://onemillion.hightower.space) and have fun!

## Using the API

Make a POST request to `http://onemillion.hightower.space/onemillion` that includes the domain you would like to check.

```
POST http://onemillion.hightower.space/onemillion

{"domain": "example.com"}
```

Here is a python snippet using the [requests](https://github.com/requests/requests) package:

```python
import requests

domain = "example.com"
r = requests.post("http://onemillion.hightower.space/onemillion", {'domain': domain})

if r.ok:
    print("{} is ranked {}".format(domain, r.text))
```
