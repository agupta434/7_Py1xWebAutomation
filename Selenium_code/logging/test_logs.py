# to capture details which are useful while debugging
# and show the user details about execution of program

# warning to users
# and information to the user
# Errors and critical error

import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)  # __name__ return the root name (file name)
    # Intentional Logging to user
    LOGGER.info("This is informational logs")
    LOGGER.warning("This is warning logs")
    LOGGER.error("This is Error logs")
    LOGGER.critical("This is Critical logs")
