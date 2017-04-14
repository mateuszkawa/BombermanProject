import tornado.web
from messages import Registration, User

registration = Registration(3000)


class RegisterREST(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", '*')
        self.set_header("Access-Control-Allow-Headers", 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", "application/json")

    def post(self: tornado.web.RequestHandler, user_name):
        user = User(user_name)
        print(user_name)
        try:
            response = registration.register(user)
            self.write(response)
        except Exception as ex:
            self.write_error(500)
