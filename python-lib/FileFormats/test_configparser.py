import configparser
import os

config_file = os.getcwd() + os.sep + "test_config.ini"


def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                          'Compression': 'yes',
                          'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'  # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    pass


def read_config():
    config = configparser.ConfigParser()
    config.read(config_file)
    # section
    print(config.sections())
    # key
    if 'bitbucket.org' in config: print(True)
    # key value
    print(config['DEFAULT']['Compression'])
    for key in config['bitbucket.org']: print(key)
    pass


def test_config():
    config = configparser.ConfigParser()
    config.read(config_file)
    # has section
    print(config.has_section('bitbucket.org'))
    # remove section
    config.remove_section('bitbucket.org')
    # add section
    section_name = 'test section'
    config.add_section(section_name)
    config.set(section_name, 'year', '2018')
    config.set(section_name, 'city', 'shenzhen')
    # save file
    with open(config_file, 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    create_config()
    read_config()
    test_config()
