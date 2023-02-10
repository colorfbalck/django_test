# -*- coding: utf-8 -*-
# @Time    : 2023-02-08 13:23
# @Author  : Test_Zhou
# @Email   : 645154096@qq.com
# @File    : chatgpt.py 
# @Software: PyCharm
import openai

# Initialize the API client with your API key
openai.organization = "org-oL3JmTdPRtrcrb9VvG0WUHfp"
openai.api_key = "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"


class Openapi:

    def generate_response(prompt):
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message


response = Openapi.generate_response("如何连续对话")
print(response)

