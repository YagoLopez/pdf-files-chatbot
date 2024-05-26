from embedchain import App
import os
import json

os.environ["OPENAI_API_KEY"] = "sk-proj-p1CKVQJ1ByiA4S6aHRYPT3BlbkFJ3HjGh84xryiP2gWRUtba"
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

config = {
  "app": {"config": {"id": "my-app"}},
  "llm": {
      "provider": "huggingface",
      "config": {
          "model": "Trendyol/Trendyol-LLM-7b-chat-v0.1",
          "local": True,  # Necessary if you want to run model locally
          "top_p": 0.5,
          "max_tokens": 1000,
          "temperature": 0.1,
      },
  }
}
app = App.from_config(config=config)
res = app.query("Where is Asturias?")
print(res)
