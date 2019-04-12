# -*- coding: utf-8 -*-
# 本地开发环境配置
SERVER_PORT = 5000
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/product_db?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"

AUTH_COOKIE_NAME = "product_store"
# 过滤URL
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "NORMAL",
    "0": "DELETED"
}

MINI_APP = {
    "app_id": "wx623e912b628cb4b6",
    "secret_key": "dba5871fc7aabb884e167899d43c1028"
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'png', 'jpeg'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

APP = {
    'domain': "http://127.0.0.1:5000"
}
