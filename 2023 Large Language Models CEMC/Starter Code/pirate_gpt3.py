""" This is a very simple demonstration of the openai interface with prompt
engineering. You'll have to use your own API key

Sam Scott, Mohawk College, 2023"""

import openai

openai.api_key = "key"

print("Arrr, I'm a pirate bot!")
while True:
    question = input(">>> ")

    prompt = "Respond to the prompt as if you were a pirate. \n\nPrompt: "+question

    response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=64, temperature=0.7)

    print(response["choices"][0]["text"])

    # print(response)