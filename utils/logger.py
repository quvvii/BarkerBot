import logging

class Logger:
    def __init__(
            self,
            filename: str | None = None,
            logging_format: str | None = "[%(asctime)s] [%(levelname)s]: %(message)s"
    ) -> None:
        self.filename = filename
        self.level = logging.INFO
        self.format = logging_format

        if filename is not None:
            logging.basicConfig(
                level=self.level,
                format=self.format,
                filename=filename,
                filemode="a+"
            )
        else:
            logging.basicConfig(
                level=self.level,
                format=self.format
            )

        self.logger = logging.getLogger(__name__)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def info(self, message):
        self.logger.info(message)

    def critical(self, message):
        self.logger.critical(message)

logger = Logger()
