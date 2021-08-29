import logging

log = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(funcName)s]')
log.setLevel(logging.DEBUG)
