""" This is a very simple demonstration of the openai interface. You will have to install openai first:

conda install openai

Then you need your own api key:

https://beta.openai.com/account/api-keys

Sam Scott, Mohawk College, 2022"""

import openai

openai.api_key = "your key here"

while True:
    question = input(">>> ")

    response = openai.Completion.create(engine="text-davinci-001", prompt=question, max_tokens=64, temperature=0.7)

    print(response["choices"][0]["text"])

    # print(response)