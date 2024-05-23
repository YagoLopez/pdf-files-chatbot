import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'sk-proj-oNJtvAVCZPZ8VC6HTsGIT3BlbkFJMV1avpdDUOlu1Yvpoafh'


# embedder:
#   provider: openai
#   config:
#     model: 'text-embedding-3-small'

# load embedding model configuration from config.yaml file
app = App.from_config(config_path="openai-config.yaml")

app.add("https://en.wikipedia.org/wiki/OpenAI")
app.query("What is OpenAI?")