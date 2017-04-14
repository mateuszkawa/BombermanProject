from tornado.testing import AsyncHTTPTestCase
from tornado.httpclient import HTTPResponse, HTTPRequest
from base.webserver import get_application
from webapp import extend_url_mapper


class MyTestCase(AsyncHTTPTestCase):
    name = 'some_name'

    def get_app(self):
        extend_url_mapper()
        return get_application(port=None)

    def test_registration(self):
        response: HTTPResponse = self.fetch('/bomber/rest/register/%s' % self.name, method='POST', body='')
        print(response)
        print(response.body)
        print(eval(response.body)['time_left'])
        self.assertIsNotNone(eval(response.body)['time_left'])

    def test_registration_via_httprequest(self):
        print('\nNew test')
        url = '/bomber/rest/register/%s_1' % self.name
        http_request = HTTPRequest(
            url=self.get_url(url),
            method='POST',
            body='')
        self.http_client.fetch(http_request, self.stop)
        response = self.wait()
        print(response)
        print(response.body)
        self.assertIsNotNone(eval(response.body)['time_left'])
