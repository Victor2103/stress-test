from locust import HttpUser, task
import os
import random
import string
from dotenv import load_dotenv
load_dotenv()

intent = ["Hello", "Hi", "Bye", "Help me",
          "can you help me ?", "WHo are you ?", "Good Morning"]

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        body = {"text": random.choice(intent),
                "message_id": ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10000))}
        self.client.post("/model/parse?emulation_mode=LUIS",
                         headers=headers, json=body)
