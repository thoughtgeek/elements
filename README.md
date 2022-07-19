# CSV data API

### Setting up:
This project requires docker and docker-compose to be built.
To build the API, at the project root run -
```
$ docker-compose up --build
```

### Available APIs:
Retrieve list of all entries
```
$ http localhost:8000/api/appdata/
HTTP/1.1 200 OK
Allow: GET
Content-Length: 104
Content-Type: application/json
Referrer-Policy: same-origin
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "id": 1,
        "title": "title"
    },
    {
        "id": 2,
        "title": "apple"
    },
    {
        "id": 3,
        "title": "computer"
    },
    {
        "id": 4,
        "title": "surya"
    }
]
```

Retrieve details of single entry
```
$ localhost:8000/api/appdata/3/
HTTP/1.1 200 OK
Allow: GET
Content-Length: 153
Content-Type: application/json
Referrer-Policy: same-origin
Vary: Accept, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "description": "computational machine",
    "id": 3,
    "image": "https://britishlibrary.typepad.co.uk/.a/6a00d8341c464853ef01bb07aa6800970d-pi",
    "title": "computer"
}
```

### Testing:
Run unit tests
`$ docker-compose exec web poetry run coverage run --source "elements" manage.py test -v 2`

Generate coverage report
`$ docker-compose exec web poetry run coverage report`

```
Name                                      Stmts   Miss  Cover
-------------------------------------------------------------
elements/__init__.py                          0      0   100%
elements/api/__init__.py                      0      0   100%
elements/api/apps.py                          4      0   100%
elements/api/migrations/0001_initial.py       5      0   100%
elements/api/migrations/__init__.py           0      0   100%
elements/api/models.py                       12      1    92%
elements/api/serializers.py                  14      0   100%
elements/api/tests.py                        27      0   100%
elements/api/views.py                        19      0   100%
elements/asgi.py                              4      4     0%
elements/settings.py                         25      0   100%
elements/urls.py                              7      0   100%
elements/wsgi.py                              4      4     0%
-------------------------------------------------------------
TOTAL                                       121      9    93%
```
