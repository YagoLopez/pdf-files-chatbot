import google.generativeai as genai
import os
from embedchain import App

os.environ["GOOGLE_API_KEY"] = "AIzaSyB5Psv-MBjqCe8e8-SK27NW_e3SHkm27Ro"

app = App.from_config(config_path="googleai-config.yaml")

app.add("https://www.forbes.com/profile/elon-musk")

response = app.query("What is the net worth of Elon Musk?")
if app.llm.config.stream: # if stream is enabled, response is a generator
    for chunk in response:
        print(chunk)
else:
    print(response)
