import streamlit as st
import openai
import json
openai.api_key=st.secrets[open_api_key]


#'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'

if 'key' not in st.session_state:

    st.session_state.key={
   
    '1': 'Ask the questions in this format "what Position are you  hiring for?"',
    '2':'Ask the questions in this format"what are the skills required for this position"',
    '3': 'Ask the questions in this format"How many years of experience is needed ?"',
    '4': 'Ask the questions in this format"What is the minimum education requirement ?"',
     '5':'Ask the questions in this format"What location is the position based in ?"',
    '6':'Ask the questions in this format"Ask Is this position remote (Yes/no)" ?',
    '7':'Give summary in the end'
    
    }


st.title("HRA Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{'role':"system","content":"Act as a hiring recruitement chatbot agent"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == 'assistant':
         
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if message["role"] == 'user':
         
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
for key in  dict(st.session_state.key):
        i=st.session_state.key[key]
  

        st.session_state.messages.append({'role':'system','content':f"{i}"})
        resp=openai.ChatCompletion.create(
                            model='gpt-3.5-turbo',
                            messages=st.session_state.messages,temperature=0.7)
        response=resp['choices'][0]['message']['content']
        with st.chat_message('Assistant'):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

        if prompt := st.chat_input("here",key=''):
            
        # Display user message in chat message container
            st.chat_message("user").markdown(st.session_state)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            del st.session_state.key[key]
            st.rerun()

        else:
            break
    
