---
title: AI Deploy - Tutorial - How to stress test an AI deploy application
slug: deploy/stress-test-an-app
excerpt: Understand how you can easily benchmarking an application and see his limitations
section: AI Deploy - Tutorials
order: 10
---

**Last updated 17th February, 2023.**

## Objective

The aim of this tutorial is to benchmarking your application. Imagine you create your application and you want to know how many GPU you will need to deploy it. How many users will use your API ? To do this, there are several applications who simulate the number of users and the number of requests you want to simulate. But let's dive a little deeper. We will use here a simple framework from python named locust. This framework is really easy to install if you have pip on your machine. Of course, there lots of others applications to stress test your apps. I can name [hey](https://github.com/rakyll/hey). This app requires to use a virtual machine so is a little more complicated to install compared to locust. You can also use [k6](https://k6.io/docs/test-types/stress-testing/). This framework is a little more complicated to install but can be use without python if you don't like the language. Lots of apps have been created to stress test your applications. Now, let's try to test our API. In this use case, the api is a spam classifier. If you're interested with this API, please check this [tutorial](https://docs.ovh.com/fr/publiccloud/ai/deploy/tuto-fastapi-spam-classifier/). Lots of others API are available on the `OVH portfolio` from AI deploy. You can found them [here](https://docs.ovh.com/fr/publiccloud/ai/deploy/apps-portfolio/). But it is not the purpose of the tutorial because you must test your API ! 

**Requirements**

- Access to the [OVHcloud Control Panel](https://www.ovh.com/auth/?action=gotomanager&from=https://www.ovh.co.uk/&ovhSubsidiary=GB);
- A Public Cloud project created;
- An API running in AI Deploy on your public cloud project. 

## Instructions


### Try our API

Say hello to the chatbot to see how it respond. Open a terminal and launch this command :
```console 
curl -s -X POST \ 
"<api_url>/model/parse?emulation_mode=LUIS" \
-H "Authorization: Bearer <token>" \
-H "Content-Type: application/json" \
-d '{"text":"Hello","message_id":"00100203"}' |jq
```

Here are a few explanations of the lines : 
- In the first line, we specify that we will use a post method. 
- We specify the url where the post request will be executed. The `api_url` is the url you get before when you create your 2 apis of rasa. You can choose the api with 4 cpus or the api with 2 gpus. It should look something like this : `https://baac2c13-2e69-4d0f-ae6b-dg9eff9be513.app.gra.ai.cloud.ovh.net/`. 
- We put the token to access our API. We specify it in the header of the request. 
- We specify that our body in in a json format.
- We put in our body the message we want to send to the chatbot. And we hope the chatbot will send us the probability of each response. The last `| jq` instruction permits to have a good display of the result in the terminal. 

Now, let's stress test our 2 APIs ! We will use the framework locust. This framework is very easy to install, it is a module from pip. This tool provides an interface where you can specify the url of your api, the number of users connected to your API, the number of calls per minute and much more. To use locust, we will deploy it as an app with the tool `AI Deploy` from OVHcloud. 

### Configure Locust to run the tests

 
### See the results with Locust


### See the results with the OVHcloud Monitoring APP


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