#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import logging

import tornado
from tornado.options import define, options

#  a util func use for connect path. eg:
#  >>> path('/a', 'b', 'c')
#  >>> '/a/b/c'
path = lambda root, *a: os.path.join(root, *a)

# some basic path settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)
STATIC_PATH = path(PROJECT_ROOT, 'static')
TEMPLATE_PATH = path(PROJECT_ROOT, "templates")
LOG_DIR = "/var/log/{{cookiecutter.project_slug}}"

# add project path to system that could importable. eg:
# >>> from {{ cookiecutter.project_slug }}.handlers import base
sys.path.insert(0, BASE_DIR)

# tornado varable define
define("port", default=8000, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

# parse commadline
tornado.options.parse_command_line()
# parse config file
if options.config:
    tornado.options.parse_config_file(options.config)

# Development type setting
class DeploymentType:
    PRODUCTION = "PRODUCTION"
    STAGING = "STAGING"
    TEST = "TEST"
    DEV = "DEV"

if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.DEV

# settings for tornado Web class `Application` init
settings = {
    "debug": DEPLOYMENT != DeploymentType.PRODUCTION or options.debug,
    "static_path": STATIC_PATH,
    "template_path": TEMPLATE_PATH,
    "cookie_secret": "!!CHANGEME!!",
    "xsrf_cookies": False
}

# logging config
# the dict of below, `root` field is for root logger, `loggers` field are
# child logger. usually, child logger is for diffrence module or scenario.
DEV_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s; %(thread)d - %(filename)s - %(funcName)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'main_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'basic',
            'filename': path(LOG_DIR, 'main.log'),
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'basic',
            'filename': path(LOG_DIR, 'error.log'),
        },
        'requests_main_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'basic',
            'filename': path(LOG_DIR, 'requests_main.log'),
        },
        'requests_error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'basic',
            'filename': path(LOG_DIR, 'requests_error.log'),
        }
    },
    'loggers': {
        '{{cookiecutter.project_slug}}.foo': {
            'handlers': ['console', 'main_file', 'error_file'],
            'level': 'DEBUG',
            'propogate': False
        },
    },
    'root': {
        'handlers': ['console', 'main_file', 'error_file'],
        'level': 'DEBUG',
    }
}

PROD_LOGGING = DEV_LOGGING.copy()
PROD_LOGGING.update({
    'loggers': {
        '{{cookiecutter.project_slug}}.foo': {
            'handlers': ['main_file', 'error_file'],
            'level': 'DEBUG',
            'propogate': False
        },
    },
    'root': {
        'handlers': ['main_file', 'error_file'],
        'level': 'DEBUG',
    }
})

LOGGING_CONF = DEV_LOGGING if settings["debug"] else PROD_LOGGING
logging.config.dictConfig(LOGGING_CONF)
