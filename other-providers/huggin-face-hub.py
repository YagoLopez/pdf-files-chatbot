import os
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

config = {
  "app": {"config": {"id": "my-app"}},
  "llm": {
      "provider": "huggingface",
      "config": {
          "model": "bigscience/bloom-1b7",
          "top_p": 0.5,
          # "max_length": 200,
          "temperature": 0.1,
      },
  },
}

app = App.from_config(config=config)
