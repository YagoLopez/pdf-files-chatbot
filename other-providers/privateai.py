from embedchain import App

app = App.from_config("config.yaml")
app.add("./docs/", data_type="directory")

while True:
    user_input = input("Ask a question (type 'exit' to quit): ")

    # Break the loop if the user types 'exit'
    if user_input.lower() == "exit":
        break

    # Process the input and provide a response
    response = app.query(user_input)
    print(response)
