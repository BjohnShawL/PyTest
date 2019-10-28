import tornado
import tornado.web

class NavigationHeader(tornado.web.UIModule):
    def render(self):
        return self.render_string("navbar.html")