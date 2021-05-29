import logging

logger = logging.getLogger(__name__)
# save in disk
logging.basicConfig(filename='api.log', level=logging.DEBUG)