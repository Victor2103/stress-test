from locust import HttpUser, task
import os
import random
from lorem_text import lorem
from dotenv import load_dotenv
load_dotenv()

messages = []

for i in range(1000):
    messages.append(lorem.paragraphs(10))

headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        body = {"message": random.choice(messages)}
        self.client.post("/spam_detection_path",
                         headers=headers, json=body)
