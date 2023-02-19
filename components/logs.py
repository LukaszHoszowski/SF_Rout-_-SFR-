import logging
import logging.handlers


def logger_configurer() -> None:
    """
        Creates instance of logger for log listener, set the configuration for logger.

            Returns:
                None
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler_f = logging.handlers.RotatingFileHandler('./logs/sfr.log', 'a',
                                                   1_000_000, 3)
    handler_s = logging.StreamHandler()
    handler_s.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)-20s| %(levelname)-8s| %(processName)-12s| '
                                  '%(message)s', '%Y-%m-%d %H:%M:%S')
    handler_f.setFormatter(formatter)
    handler_s.setFormatter(formatter)
    
    logger.addHandler(handler_f)
    logger.addHandler(handler_s)