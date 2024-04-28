""" This is a very simple skeleton for a FAQ bot, based on the handout given in
class. Your job is to create your own FAQ bot that can answer 20 questions
using basic string matching. See the handout for more details.

When you create your bot you can adapt this code or start from scratch and
write your own code.

If you adapt this code, add yourself below as author and rewrite this header
comment. See the Resources folder on Canvas for documentation standards.

YOUR NAME AND DATE
Sam Scott, Mohawk College, May 2021
"""

def load_FAQ_data():
    """This method returns a list of questions and answers. The
    lists are parallel, meaning that intent n pairs with response n."""

    global questions
    global answers

    questions = [
        "What is this?",
        "What are the components of a chat bot?"
    ]

    answers = [
        "This is a very simple FAQ bot skeleton. Flesh this out into your very own FAQ bot.",
        "The basic chat bot pipeline consists of the following components: Speech Recognition, Natural Language Understanding, Dialog Management, Natural Language Generation, and Text to Speech Synthesis. Not all chat bots use every component."
    ]

    return questions, answers

def understand(utterance):
    """This method processes an utterance to determine which intent it
    matches. The index of the intent is returned, or -1 if no intent
    is found."""

    global intents # declare that we will use a global variable

    try:
        return intents.index(utterance)
    except ValueError:
        return -1

def generate(intent):
    """This function returns an appropriate response given a user's
    intent."""

    global responses # declare that we will use a global variable

    if intent == -1:
        return "Sorry, I don't know the answer to that!"

    return responses[intent]

## Main Program

# Get the intents and responses
intents, responses = load_FAQ_data()

# talk to the user
print("Hello! I know stuff about chat bots. When you're done talking, just say 'goodbye'.")
print()
utterance = ""
while True:
    utterance = input(">>> ")
    if utterance == "goodbye":
        break;
    intent = understand(utterance)
    response = generate(intent)
    print(response)
    print()

print("Nice talking to you!")
