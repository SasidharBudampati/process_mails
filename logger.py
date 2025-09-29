import logging
import os
from logging.handlers import RotatingFileHandler
from loadenv import LOG_FILE_PATH, LOG_LEVEL, LOG_MAX_BYTES, LOG_BACKUP_COUNT

def get_logger(name: str = "DefaultLogger") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        level = getattr(logging, LOG_LEVEL.upper(), logging.DEBUG)
        logger.setLevel(level)

        log_dir = os.path.dirname(LOG_FILE_PATH)
        os.makedirs(log_dir, exist_ok=True)

        # ✅ Always add file handler
        file_handler = RotatingFileHandler(
            LOG_FILE_PATH,
            maxBytes=5 * 1024 * 1024,
            backupCount=LOG_BACKUP_COUNT,
            encoding="utf-8"
        )
        file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # ✅ Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger