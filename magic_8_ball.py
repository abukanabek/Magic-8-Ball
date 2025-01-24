import random
import time

ball8 = '''        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........'''

answers = [
    "Without a doubt", "It is certain", "No doubts", "Definitely yes",
    "You can rely on it", "It seems to me - yes", "Most likely",
    "Good prospects", "Signs point to yes", "Yes", "Unclear for now, try again",
    "Ask later", "Better not to tell", "Cannot predict now",
    "Concentrate and ask again", "Don't even think about it", "My answer is no",
    "According to my data - no", "Not very promising", "Very doubtful"
]

print("I am the russian-speaking 8-ball... Ask me anything you'd like...")
print(ball8)

def ask_question():
    print("Ok, what are you bothered by?")
    
    question = input()
    print(random.choice(answers))
    time.sleep(1)
    print("Want to ask more questions? (yes/no)")
    if input().lower().startswith('n'):
        print("I'll see you some day...")
        return True
    return False    

while ask_question()!=True:
    ask_question()