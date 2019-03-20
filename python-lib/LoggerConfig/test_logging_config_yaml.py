import yaml
import logging.config
import os


def setup_logging(default_path='config_yaml.yaml', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt', encoding="utf8") as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        print('the input path doesn\'t exist')


setup_logging(default_path='config_yaml.yaml')
logger = logging.getLogger()
logger.info("hello world")