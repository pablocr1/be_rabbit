import datetime
import os
import yaml

try:
    APP_ENV = str(os.environ['APP_ENV'])
except KeyError:
    APP_ENV = 'development'

ROOT = os.path.dirname(os.path.abspath(__file__))
print(ROOT)

def load_config_file(name: str, noenv=0):
    if noenv == 1:
        return yaml.safe_load(open(ROOT + "/app/ymls/{}.yml".format(name), 'r', encoding="utf-8"))
    return yaml.safe_load(open(ROOT + "/app/ymls/{}.yml".format(name), 'r'))[APP_ENV]

DATABASE = load_config_file('database')

class Config:
    print("Hello")