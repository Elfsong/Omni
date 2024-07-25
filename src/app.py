# coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 24

import time
import utils
import streamlit as st

st.image('./resource/img/Omni_logo.png')

query = st.text_input(
    label="search_field",
    placeholder="Answer Anything Here",
    label_visibility='collapsed'
)


if query:
    context = ""
    
    with st.status(f'[Gloabl Search Engine] Retrieval documents for [{query}]...'):
        global_result = utils.global_retrieval(query)
        st.write(global_result)
        context += str(global_result)
    
    with st.status(f'[Cisco Search Engine] Retrieval documents for [{query}]...'):
        url_list = utils.cisco_retrieval(query)
        for url_pair in url_list:
            title, url, content_list = url_pair
            content = " ". join(content_list)
            # content = utils.extraction(url)
            context += content
            st.html(f'🌟 <a href="{url}" style="color: black;">{title}</a>')
    
    with st.spinner('[CoT Engine] Generating Results...'):
        response = utils.response(query, context)
    
    st.markdown(response)


