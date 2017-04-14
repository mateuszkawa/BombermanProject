import base.webserver as webserver
from base.webserver import start
from rest.register import RegisterREST
from rest.messages import StateREST


def extend_url_mapper():
    webserver.url_mapper.extend((
        (r"/bomber/rest/register/(.*)", RegisterREST),
        (r"/bomber/rest/state/(.*)", StateREST)
    ))


if __name__ == '__main__':
    extend_url_mapper()
    port = 9800
    start(port)
