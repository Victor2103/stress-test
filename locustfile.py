# Import the dependecies of locust
from locust import HttpUser, task
# Import general library from python
import os
import random
# Import lorem ipsum library to generate some text
from lorem_text import lorem
# Import dotenv to load the environments variables
from dotenv import load_dotenv
load_dotenv()

# Create a table with some lorem ipsum texts
messages = []

# Add 1000 random texts of 10 paragraphs each (simulate 1000 emails)
for i in range(1000):
    messages.append(lorem.paragraphs(10))

# Define the headers of the request
headers = {
    "Authorization": f"Bearer {os.getenv('TOKEN')}", "Content-Type": "application/json"}


class HelloWorldUser(HttpUser):
    # Definition of the first path where we do our post request
    @task
    def hello_world(self):
        # Define the body with the email choose randomly from the tab of all the emails
        body = {"message": random.choice(messages)}
        # Do the post request on the spam detection path
        self.client.post("/spam_detection_path",
                         headers=headers, json=body)
