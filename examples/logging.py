import logging
import logging.config

# It's possible you might need to use this:
# logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.conf'), disable_existing_loggers = False)
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)