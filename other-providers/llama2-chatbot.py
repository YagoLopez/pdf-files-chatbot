import os
from embedchain import App

os.environ["REPLICATE_API_TOKEN"] = "r8_91cuckBglEjl6lFduCtYULJyrEtpZZW1i8FYD"

# config = {
#   "llm": {
#     "provider": "llama2",
#     "config": {
#       "model": "a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
#       "temperature": 0.5,
#       "max_tokens": 1000,
#       "top_p": 0.5,
#       "stream": False
#     }
#   }
# }
#
# load llm configuration from config.yaml file
app = App.from_config(config_path="llama2-config.yaml")
