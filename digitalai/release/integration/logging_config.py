import sys
import logging.config
LOGGING_CONFIG = ({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)-7s [%(filename)s:%(lineno)d] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'Digitalai': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        },
        '__main__': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': False
    }
})
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("Digitalai")
