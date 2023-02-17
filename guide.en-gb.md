---
title: AI Deploy - Tutorial - How to stress test an AI deploy application
slug: deploy/stress-test-an-app
excerpt: Understand how you can easily benchmarking an application and see his limitations
section: AI Deploy - Tutorials
order: 10
---

**Last updated 17th February, 2023.**

## Objective

The aim of this tutorial is to benchmarking your application. Imagine you create your chatbot and you want to know how many GPU you will need to deploy it.  To do this, there are several applications who permits to easily test your API. But how can they test your APIs ? It is easy. They just simulate a number of user you want, the number of calls they make in your API per minute or seconds. The objective is to see the limits of number of calls on the API. In our example, we will use the API of a rasa chatbot already deployed. We will consider that there are 1000 users and every seconds, there 100 users who make a request on the API. So how many CPU/GPU I need ? How can I know my app will not crash. Let's try it. We will deploy two API of the same chatbot. One API will have 4 cpus and the second API will use 1 GPU. To simulate the users we will use the module Locust. Of course, there lots of others applications to stress test your apps. But locust is really easy to install and to use. It is a very good start to understand the purpose of this tutorial. 

**Requirements**

- Access to the [OVHcloud Control Panel](https://www.ovh.com/auth/?action=gotomanager&from=https://www.ovh.co.uk/&ovhSubsidiary=GB);
- A Public Cloud project created;
- The ovhai CLI interface installed on your laptop. More information [here](https://docs.ovh.com/gb/en/publiccloud/ai/cli/install-client/);
- A [user for AI Deploy](https://docs.ovh.com/gb/en/publiccloud/ai/users/);
- [Docker](https://www.docker.com/get-started) installed on your local computer;
- Some knowledge about building image and [Dockerfile](https://docs.docker.com/engine/reference/builder/).

## Instructions

### Create our 2 apis for the chatbot. 

The chatbot is a simple rasa chatbot. The purpose of this tutorial is not to create or deploy the chatbot. Please go [here](https://docs.ovh.com/fr/publiccloud/ai/) if you want to do this. So now, let's deploy two apps, one with 1 GPU and the other with 4 cpu. To do this, let's first clone this [repo git](https://github.com/Victor2103/stress-test) ! 

Once he is cloned, we will create the Dockerfile to build the API of the chatbot !

To do so, we will specify the parent directory image we will use :

```console
FROM python:3.8
```

Then we specify the repository we will copy in our dockerfile. 

```console
WORKDIR /workspace
ADD . /workspace
```

We install all of the requirements of rasa. This requirements permits to launch the api of rasa, our chatbot. 

```console
RUN pip install --no-cache-dir -r requirements_rasa.txt
```

Then we say to OVHcloud we want to run the dockerfile as a user 420420. 

```console
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
```

You specify the command to run the docker container and we specify the port where we will expose our chatbot. 
```console
EXPOSE 5005 
CMD rasa run --enable-api 
```
Our dockerfile is now created. Let's put it inside the folder `chatbot` in our git repository, name it chatbot.Dockerfile and let's create the image ! If you want to directly create the image, the dockerfile is [here](https://github.com/Victor2103/stress-test/blob/dev/chatbot/chatbot.Dockerfile) you have no need to create it. 

Now, let's create the image. Just run this command on the root of the folder :

```bash
docker build . -f chatbot.Dockerfile -t rasa-api:latest
```

You can now push this docker image in your repository dockerhub or in your private directory docker directly on OVHcloud. More information about this can be found [here](https://docs.ovh.com/fr/publiccloud/ai/training/add-private-registry/).

To push it on your private directory registry you can follow this little tutorial. 

```console
ovhai registry list
```

Login on the shared registry with your usual OpenStack credentials:

```console
docker login -u <user> -p <password> <shared-registry-address>
```

Push the compiled image into the shared registry:

```console
docker tag rasa-api:latest <shared-registry-address>/rasa-api:latest
docker push <shared-registry-address>/rasa-api:latest
```


You want to test it locally. No problem, run the command above :
```bash
docker run --rm -it -p 5005:5005 --user=42420:42420 rasa-api:latest
```

Ok, now let's deploy on OVHcloud to api of rasa, one with one GPU and one with 4 cpus. It is really easy, you just have to run two commands in the same terminal. Here are they :
```bash
ovhai app run --name rasa-api-4-cpu \
--cpu 4 \
--default-http-port 5005 \
<shared-registry-address>/rasa-api:latest
```

And for 1 GPU, just run :
```bash
ovhai app run --name rasa-api-4-cpu \
--gpu 1 \
--default-http-port 5005 \
<shared-registry-address>/rasa-api:latest
```

Ok, now our apps should be available. You can go on the URL provide by OVHcloud, you will just see a message with Hello from Rasa. Let's now try our API with a simple curl in the terminal. 

### Try our API



## Go further

If you want to use more functionnality about Rasa, please fill free to go into this link. We use Rasa Open Source and not Rasa X. 

[Rasa Open source](https://rasa.com/docs/rasa/)

If you want to deploy your model created with the chatbot, you can follow this tutorial. 

[How to deploy a chatbot](https://confluence.ovhcloud.tools/display/~victor.vitcheff@corp.ovh.com/Part+3+deploy+your+rasa+chatbot+with+a+simple+django+app)

If you want to train a rasa chatbot with the tool AI Training, please look at this tutorial .

[How to train a chatbot with only one docker file](https://confluence.ovhcloud.tools/display/~victor.vitcheff@corp.ovh.com/Part+2+Train+a+rasa+chatbot+with+one+docker+file)

## Feedback

Please send us your questions, feedback and suggestions to improve the service:

- On the OVHcloud [Discord server](https://discord.com/invite/vXVurFfwe9)