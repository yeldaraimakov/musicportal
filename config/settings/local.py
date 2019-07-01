from .base import *

ROOT_DIR = environ.Path(__file__) - 3

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'info_logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': ROOT_DIR.path('logs/info.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'info_logger': {
            'handlers': ['info_logfile', 'console'],
            'level': 'INFO'
        },

    }
}
