import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../libs"))

import pyperclip
import openai

openai.api_key = sys.argv[1]
keywords = sys.argv[2]

def calc_action(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            return "英文"
    return "中文"

action = calc_action(keywords)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": ("将内容'%s'翻译成%s" % (keywords, action))}
    ]
)

result = completion.choices[0].message.content.strip('"')
pyperclip.copy(result)
print(result)




