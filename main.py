import webapp2
import os
from google.appengine.ext.webapp import template #also added


class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, {}))

class Facebook(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/facebook.html')
        self.response.out.write(template.render(path, {}))

class Trends(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'templates/trends.html')
        self.response.out.write(template.render(path, {}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/facebook', Facebook),
    ('/trends', Trends),
], debug=True)
