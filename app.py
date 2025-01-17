import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


## Functions To get response from LLama 2 model

def getLLamaresponse(input_text,no_words,blog_style):
    llm = CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,'temperature':0.01})
    
 
    template =""""
write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    
    """

    prompt = PromptTemplate(template=template, input_variables=["input_text","blog_style","no_words"])


    ## generate the response from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response









st.set_page_config(page_title="Generate Blog",
                   page_icon="🧊",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs")


input_text = st.text_input("Enter the Blog Topic")



## creating to more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("writing the blog for",('Research', 'Datascientist','common'),index=0)


submit = st.button("Generate ")

##result
if submit:
    st.write(getLLamaresponse(input_text,no_words, blog_style))