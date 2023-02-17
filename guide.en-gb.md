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


