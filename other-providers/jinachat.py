import os
from embedchain import App

os.environ["OPENAI_API_KEY"] = "sk-proj-p1CKVQJ1ByiA4S6aHRYPT3BlbkFJ3HjGh84xryiP2gWRUtba"
os.environ["JINACHAT_API_KEY"] = "1NTaFkxSGgzOSP4HzjT3:bb0ba317e40c9983a9b6056caa8c8688190ae554af7a1cc5117e0141003d3f2c"

config = {
  "llm": {
    "provider": "jina",
    "config": {
      "temperature": 0.5,
      "max_tokens": 1000,
      "top_p": 1,
      "stream": False
    }
  }
}

# load llm configuration from config.yaml file
app = App.from_config(config=config)
app.add("./docs/datasource.pdf", data_type="pdf_file")

res = app.query("What is the net worth of Elon Musk?")
print(res)
