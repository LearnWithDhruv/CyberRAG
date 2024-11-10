import logging
from src.utils.logger import logger

def handle_exception(e, custom_message="An error occurred"):
    logger.error(f"{custom_message}: {str(e)}")
    print(f"{custom_message}. Check logs for details.")
