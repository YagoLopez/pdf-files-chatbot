import os
from embedchain import App

# Set your API key here or pass as the environment variable
# os.environ["GROQ_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "sk-proj-p1CKVQJ1ByiA4S6aHRYPT3BlbkFJ3HjGh84xryiP2gWRUtba"
groq_api_key = "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"

config = {
    "llm": {
        "provider": "groq",
        "config": {
            "model": "mixtral-8x7b-32768",
            "api_key": groq_api_key,
            "stream": True
        }
    }
}

app = App.from_config(config=config)
# Add your data source here
app.add("https://docs.embedchain.ai/sitemap.xml", data_type="sitemap")
app.query("Write a poem about Embedchain")

# In the realm of data, vast and wide,
# Embedchain stands with knowledge as its guide.
# A platform open, for all to try,
# Building bots that can truly fly.

# With REST API, data in reach,
# Deployment a breeze, as easy as a speech.
# Updating data sources, anytime, anyday,
# Embedchain's power, never sway.

# A knowledge base, an assistant so grand,
# Connecting to platforms, near and far.
# Discord, WhatsApp, Slack, and more,
# Embedchain's potential, never a bore.
