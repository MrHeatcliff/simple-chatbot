# Abstract

This is a Vietnamese chatbot using LLM and RAG

You can change your model and Embedded vector by yourself, but your model must be open on Huggingface

Interface was building using Gradio

# Where is Data

I use vietnamese_ecormmerce_alpacar dataset for being Document database for RAG.

You can access the data at this link: [Dataset](https://huggingface.co/datasets/5CD-AI/Vietnamese-Ecommerce-Alpaca/viewer/default/train?p=2&row=205)

# Model

For this assignment, i use NlpHUST/gpt2-vietnamese model ([Model](https://huggingface.co/datasets/5CD-AI/Vietnamese-Ecommerce-Alpaca/viewer/default/train?p=2&row=205))

# Build and deploy with docker

Run these command by sequence to build image and deploy with docker-compose

```
docker build -t chatbot .
docker-compose up --build
```

If you just want to run the container, run this instead of second line:
```
docker run -p 7860:7860 <image id>
```

Remember this take so much time to run, so be paitient. After build complete, you can access to chatbot at: localhost:7860