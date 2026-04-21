import logging
import logging.config
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(
    log_level: str = "INFO",
    log_file: str = "logs/app.log",
):
    log_path = Path(log_file)

    if log_path.parent != Path("."):
        log_path.parent.mkdir(parents=True, exist_ok=True)

    LOGGING_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "standard": {
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "standard",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": log_level,
                "formatter": "detailed",
                "filename": log_file,
                "maxBytes": 5 * 1024 * 1024,  # 5MB
                "backupCount": 5,
                "encoding": "utf8",
            },
        },

        "root": {
            "level": log_level,
            "handlers": ["console", "file"],
        },
    }

    logging.config.dictConfig(LOGGING_CONFIG)