import json
from jsonschema import validate
from os.path import exists
from lang import LANG_ERRORS
from settings import *

schema_screen = {
  "type": "object",
  "title": "Screen",
  "properties": {
    "width": {
      "type": "number",
      "title": "Width"
    },
    "height": {
      "type": "number",
      "title": "Height"
    },
    "fullscreen": {
      "type": "boolean",
      "title": "Fullscreen"
    }
  },
  "required": [
    "width",
    "height",
    "fullscreen"
  ]
}

schema_cheats = {
  "type": "object",
  "title": "Cheats",
  "properties": {
    "god_mode": {
      "type": "boolean",
      "title": "God Mode"
    }
  },
  "required": [
    "god_mode"
  ]
}

config_schema = {
  "title": "Config",
  "type": "object",
  "properties": {
    "screen": schema_screen,
    "cheats": schema_cheats
  },
  "required": [
    "screen",
    "cheats"
  ]
}

def load_config():
  try:
    config_exists = exists(CONFIG_PATH)
    if(not config_exists):
      return { "error": True, "error_message": LANG_ERRORS['MISSING_CONFIG'] }
    with open(CONFIG_PATH) as f: s = f.read()
    config = json.loads(s)
    validate(instance=config, schema=config_schema)
    return { "error": False, "payload": config }
  except:
    return { "error": True, "error_message": LANG_ERRORS['CANNOT_PROCESS_CONFIG'] }

def save_config(config):
  try:
    validate(instance=config, schema=config_schema)
    json_string = json.dumps(config, indent=4)
    with open(CONFIG_PATH, "w+") as f: s = f.write(json_string)
    return { "error": False, "payload": True }
  except:
    return { "error": True, "error_message": LANG_ERRORS['CANNOT_WRITE_CONFIG'] }
