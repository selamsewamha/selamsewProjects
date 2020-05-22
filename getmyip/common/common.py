import logging
import yaml
import os
import sys

def setup_logger(level):
  logging.basicConfig(level=level)

def get_url():
  built_path = os.path.join(sys.prefix, 'configurations', 'getmyip.yaml')
  dev_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'configurations', 'getmyip.yaml'))
  if os.path.exists(built_path):
    path = built_path
  else:
    path = dev_path
  with open(path, 'r') as f:
    return yaml.load(f)['url']
