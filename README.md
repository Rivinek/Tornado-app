# Tornado-app
Fun project on top of cool technologies.

## Techonologies

* [Python 2.7.12](https://www.python.org/)
* [Tornado](http://www.tornadoweb.org/en/stable/index.html)
* [Docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)


## File structure
```
.
├── LICENSE
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   ├── settings.py
│   └── utils
│       ├── __init__.py
│       ├── base.py
│       └── db_config.py
├── docker-compose.yml
├── env
├── env.base
└── nginx
    ├── Dockerfile
    └── sites-enabled
        └── project_boilerplate
```