import tornado.web
import
from messages import Registration, User
from engine import Engine

registration = Registration(3000)


class StateREST(tornado.web.RequestHandler):

    def __init__(self):
        self.engine = Engine()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", '*')
        self.set_header("Access-Control-Allow-Headers", 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Content-Type", "application/json")

    def get(self: tornado.web.RequestHandler, user_id):
        state = self.engine.get_state()
        self.write(response)
