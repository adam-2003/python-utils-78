import logging

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self._log(logging.DEBUG, msg)

    def info(self, msg):
        self._log(logging.INFO, msg)

    def warning(self, msg):
        self._log(logging.WARNING, msg)

    def error(self, msg):
        self._log(logging.ERROR, msg)

    def critical(self, msg):
        self._log(logging.CRITICAL, msg)

    def _log(self, level, msg):
        if not isinstance(msg, str):
            raise ValueError('Message must be a string')
        self.logger.log(level, msg)