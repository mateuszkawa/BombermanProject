import tornado.web
import tornado.ioloop

if 'url_mapper' not in globals() and 'url_mapper' not in locals():
    url_mapper = []


def get_application(port: int = 9800) -> tornado.web.Application:
    application = tornado.web.Application(url_mapper)
    if port is not None:
        application.listen(port)
    return application


def start(port: int):
    get_application(port)
    print('info services listening on {port}'.format(port=port))
    tornado.ioloop.IOLoop.instance().start()

