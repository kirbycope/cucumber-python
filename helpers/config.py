from dotenv import load_dotenv, find_dotenv
import configparser
import os


def from_config(key):
    config_file = "altunity" # from_env("CONFIG")
    config = configparser.ConfigParser()
    config.read(config_file + ".ini")
    return config["DEFAULT"][key]


def from_env(key):
    load_dotenv(find_dotenv())
    return os.environ.get(key)
