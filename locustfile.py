from locust import HttpUser, task
import os
import random
import string
from dotenv import load_dotenv
load_dotenv()

messages = ["Weel done, you win a TV", "Hi, can you help me", "This is a message", "CLick here",
          "Here is the newsletter ", "Hello, are you free this afternoon to eat", "Here is your invoice from last week"]

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        body = {"message": random.choice(messages)}
        self.client.post("/spam_detection_path",
                         headers=headers, json=body)
