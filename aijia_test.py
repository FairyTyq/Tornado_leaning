#coding:utf-8

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os
from tornado.web import StaticFileHandler


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",price1=100,price2=201)

if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
        (r'/',IndexHandler),
        (r'/(.*)',StaticFileHandler,{"path":os.path.join(current_path,"statics/html"),"default_filename":"index.html"}),
        ],
        debug = True,
        static_path = os.path.join(current_path,"statics"),
        template_path = os.path.join(current_path,"template"),
        )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    
    tornado.ioloop.IOLoop.current().start()
