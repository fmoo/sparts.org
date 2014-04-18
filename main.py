from sparts.vservice import VService
from sparts.tasks.tornado import TornadoHTTPTask

from tornado.web import RequestHandler

class WebApp(TornadoHTTPTask):
    class RedirectToGithub(RequestHandler):
        def initialize(self, task):
            self.task = task

        def get(self, trailer=None):
            self.task.logger.info("GET /%s", trailer)
            self.redirect('https://github.com/facebook/sparts')

    def getApplicationConfig(self):
        return [
            ('/(.*)', self.RedirectToGithub, {'task': self})
        ]

WebApp.register()

if __name__ == '__main__':
    VService.initFromCLI()
