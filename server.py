# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from hello import application
import logging
logging.basicConfig(level=logging.INFO)


httpd = make_server('', 8000, application)


# 启动服务
logging.info('8000 is running')
httpd.serve_forever()
