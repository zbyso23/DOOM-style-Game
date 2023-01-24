import json
from jsonschema import validate
from os.path import exists
from lang import LANG_ERRORS
from settings import *

schema = {
    "type": "object",
    "properties": {
        "width": {"type": "number"},
        "height": {"type": "number"},
        "fullscreen": {"type": "boolean"},
    },
    "required": ["width", "height", "fullscreen"],
    "additionalProperties": False
}

def load_config():
  try:
    config_exists = exists(CONFIG_PATH)
    if(not config_exists):
      return { "error": True, "error_message": LANG_ERRORS['MISSING_CONFIG'] }
    with open(CONFIG_PATH) as f: s = f.read()
    config = json.loads(s)
    validate(instance=config, schema=schema)
    return { "error": False, "payload": config }
  except:
    return { "error": True, "error_message": LANG_ERRORS['CANNOT_PROCESS_CONFIG'] }
