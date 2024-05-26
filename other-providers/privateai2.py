import os
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

from embedchain import App

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}

app = App.from_config(config=config)
app.add("./docs/datasource.pdf", data_type="pdf_file")
# res = app.query("Is is worth to visit Asturias?")
# print("Answer:", res)

while True:
    user_input = input("Ask a question about Asturias (type 'exit' to quit): ")

    # Break the loop if the user types 'exit'
    if user_input.lower() == "exit":
        break

    # Process the input and provide a response
    response = app.chat(user_input)
    print(response)