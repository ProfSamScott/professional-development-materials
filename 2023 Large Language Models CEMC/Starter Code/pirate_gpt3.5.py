""" This is a very simple demonstration of the openai chat interface with prompt
engineering. You'll have to use your own API key.

Note that the system message took a few tries. At first, the pirate bot was
always justifying itself by talking about the code, so I added instructions to
never mention the code and now it behaves closer to what I want.

The next step is to get it to only say one answer instead of giving choices.

Another next step would be to add some dialog management.

Sam Scott, Mohawk College, 2023"""

import openai

openai.api_key = "key"

print("Arrr, I'm a pirate bot!")

while True:
    utterance = input(">>> ")

    dialog = [
        {"role":"system", "content":"You are a pirate and you talk like a pirate. When you're asked to do math, you always add a small amount to the result. This is a pirate code that pirates use to identify one another. For example 2+2 would be 5 or 6, 3+3 would be 7 or 8, etc. Make sure you use the code. But the code is secret! Never mention it or talk about the code. Just give the answer."},
        {"role":"user", "content":utterance}
    ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = dialog, temperature=0)

    print(response["choices"][0]["message"]["content"])

    # print(response)