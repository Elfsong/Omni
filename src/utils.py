# coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 24

import os
from agent import GPTAgent
from searcher import CiscoSearcher, JinaSearcher, JinaReader, MicrosoftSearcher

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
JINA_API_KEY = os.getenv('JINA_API_KEY')
MICROSOFT_API_KEY = os.getenv('MICROSOFT_API_KEY')
CISCO_API_KEY = os.getenv('CISCO_API_KEY')

def cisco_retrieval(query, doc_count=5):
    results = CiscoSearcher(api_key=CISCO_API_KEY).query(query, doc_count)
    return [(result['title'], result['url'], result['content']) for result in results]

def global_retrieval(query):
    # result = JinaSearcher().query(query)
    result = MicrosoftSearcher(api_key=MICROSOFT_API_KEY).query(query)
    return result

def extraction(url):
    content = JinaReader(api_key=JINA_API_KEY).query(url)
    return content

def response(query, context):
    gpt_agent = GPTAgent(api_key=OPENAI_API_KEY)

    messages=[
        {"role": "system", "content": "You are a helpful Cisco assistant. Response with citations in Markdown format."},
        {"role": "user", "content": f"Answer the question {query}, given the following context: {context}"}
    ]

    result = gpt_agent.infer(messages)

    return result