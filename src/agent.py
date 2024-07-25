# coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 24

from openai import OpenAI

class GPTAgent():
    def __init__(self, api_key) -> None:
        self.client = OpenAI(api_key=api_key)
        
    def infer(self, messages):
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )

        return completion.choices[0].message.content