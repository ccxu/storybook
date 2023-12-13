from prompt import Prompt
import requests
import json
import os



open_api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = "gpt-4-1106-preview"
        self.model_url = "https://chatapi.onechat.fun/v1/chat/completions"
        self.temperature = 0.7
        self.max_tokens = 500

    def get_response(self):
        headers = {"Content-Type": "application/json", "Authorization":open_api_key}
    
        pload = {
            "model": self.model,                               
            "messages": self.add_msg(),
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        response = requests.post(self.model_url,
                                headers=headers,
                                json=pload,
                                stream=True)
        data = response.json()
        result = data["choices"][0]["message"]["content"]
        return result

    def add_msg(self, text):
        self.prompt.add_msg(text)
