import os
from embedchain import App
import json

text_file = open('../docs/plain-text.txt', 'r')
text_file_contents = text_file.read()
text_file.close()

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "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"

config = {
    'llm': {
        'provider': 'huggingface',
        'config': {
            'model': 'mistralai/Mistral-7B-Instruct-v0.2',
            'top_p': 0.5,
            'stream': True,
        },
    },
    'embedder': {
        'provider': 'huggingface',
        'config': {
            'model': 'sentence-transformers/all-mpnet-base-v2'
        }
    }
}

app = App.from_config(config=config)
app.add(text_file_contents, data_type="text")

while True:
    user_input = input("Ask a question about Asturias (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    # (response, sources) = app.query(user_input, citations=True)
    # print("========================================")
    # print(response)
    # print("========================================")
    # print(json.dumps(sources, indent=4, sort_keys=False))

    response2 = app.chat(user_input)