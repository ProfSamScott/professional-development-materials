""" This is a very simple demonstration of the openai chat interface. You'll have to use your own API key.

Using the information in the handout on the chat API, see if you can
add dialog management.

Sam Scott, Mohawk College, 2023"""

import openai

openai.api_key = "..."

while True:
    utterance = input(">>> ")

    dialog = [
        {"role":"system", "content":"You are a helpful assistant"},
        {"role":"user", "content":utterance}
    ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = dialog, temperature=0)

    print(response["choices"][0]["message"]["content"])
    dialog.append(r["choices"][0]["message"])
    # print(response)