import logging.config
import os

from django.utils.log import DEFAULT_LOGGING


def heroku_logging_config(**options):
    log_level = options.get('LOG_LEVEL')
    sentry_log_level = options.get('SENTRY_LOG_LEVEL')

    return logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                # exact format is not important, this is the minimum information
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            },
            'django.server': DEFAULT_LOGGING['formatters']['django.server'],
        },
        'handlers': {
            # console logs to stderr
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },

            # Add Handler for Sentry for `warning` and above
            'sentry': {
                'level': sentry_log_level,
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },

            'django.server': DEFAULT_LOGGING['handlers']['django.server'],
        },
        'loggers': {
            # default for all undefined Python modules
            '': {
                'level': 'WARNING',
                'handlers': ['console', 'sentry'],
            },
            # Our application code
            'utils': {
                'level': log_level,
                'handlers': ['console', 'sentry'],
                # Avoid double logging because of root logger
                'propagate': False,
            },
            'meals': {
                'level': log_level,
                'handlers': ['console', 'sentry'],
                # Avoid double logging because of root logger
                'propagate': False,
            },
            'members': {
                'level': log_level,
                'handlers': ['console', 'sentry'],
                # Avoid double logging because of root logger
                'propagate': False,
            },
            # # Prevent noisy modules from logging to Sentry
            # 'noisy_module': {
            #     'level': 'ERROR',
            #     'handlers': ['console'],
            #     'propagate': False,
            # },
            # Default runserver request logging
            'django.server': DEFAULT_LOGGING['loggers']['django.server'],
        },
    })