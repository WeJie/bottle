# -*- coding:utf-8 -*-
import sys
from bottle import route, run, BaseController, template


@route('/hello')
def hello():
    args = [sys.executable] + sys.argv
    print args
    return "Hello World!"


@route('/tpl')
def hello_tpl():
    return


@route('/')
def index():
    return "Here is index"


@route('/hello/:username')
def hello_to(username):
    return "hello %s" % username


@route('hello/{action}', action='get_name')
class MyController(BaseController):

    @staticmethod
    def get_name():
        return 'controller'


run(host='localhost', port=8080, debug=True)

{
    'wsgi.multiprocess': False,
    'wsgi.multithread': True,
    'wsgi.url_scheme': 'http',
    # 'wsgi.file_wrapper': <class wsgiref.util.FileWrapper at 0x10d6228d8 >,
    # 'wsgi.input': < socket._fileobject object at 0x10d22a650 >,
    # 'wsgi.errors': < open file '<stderr>', mode 'w' at 0x10d0e21e0 >,
    'wsgi.version': (1, 0),
    'wsgi.run_once': False,
    'HTTP_HOST': '0.0.0.0:8080',
    'HTTP_CACHE_CONTROL': 'max-age=0',
    'HTTP_CONNECTION': 'keep-alive', 'PATH_INFO': '/',
    'HTTP_COOKIE': 'sc=mQLGWxkM092OYqNepxEEQipZoDW09jm8; \
                    sentrysid="gAJ9cQFYCgAAAHRlc3Rjb29raWVYBgAAAHdvcmtlZHECcy4:1eCgv8:rR5cRyZsDkRP8hyygycPyck_mPM"; \
                    session_id=6e4cc62e4a6c569c8f5e5897f5ac829516ddd6e8; \
                    fldt=hide; \
                    session=.eJw9kMtuwjAQRX-l8ppF6sAGiUUrB8RiJjJyYs1skEpCnIdbKYAgg_j3Uhb9gHOP7rmr_XGsT0Etz-Olnql9W6nlXb19qaVik2kQO6HYOepMsztoiHQlvdVsyp79LuCGW-4-hLvtAt16IPkMYKqQO9C5swICNxJK0RcTSJOgKQQ2RQra6j8md2VLUtzQNROYfkKHAV3VgwENHQY2IYLZJuzLFroqsM-E_JPzuxZMM8eIgaRfqcdMHU7jcX_-6evv_wsUi6e67NjbK0e7YA8JRppArwcwVihmAm43gM4WKEVKkqXUrF5zl1M9vnKod_X4BWDzYPI.DOoEng.zKth91g_Z3B6THOZj4WtZmLpeKk',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate',
    'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'HTTP_DNT': '1',
    'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'SERVER_PORT': '8080',
    'SERVER_SOFTWARE': 'WSGIServer/0.1 Python/2.7.10',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'SERVER_NAME': '1.0.0.127.in-addr.arpa',
    'REQUEST_METHOD': 'GET',
    'CONTENT_TYPE': 'text/plain',
    'CONTENT_LENGTH': '',
    'GATEWAY_INTERFACE': 'CGI/1.1',
    'QUERY_STRING': '',
    'REMOTE_ADDR': '127.0.0.1',
    'SCRIPT_NAME': '',
    'LC_CTYPE': 'UTF-8',
    'LC_ALL': 'en_US.UTF-8',
    '_': '/usr/bin/python',
    'PATH_INFO': '/'
}
