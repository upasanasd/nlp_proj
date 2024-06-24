import streamlit as st
#for nlp processing
import spacy
#for visualizing 
from spacy import displacy
#extracting text from online news articles
from newspaper import Article

#loading the english language model
nlp = spacy.load("custom_ner_model")

st.title('Named Entity Recognition Demo')

article_url = st.text_input('Enter URL')

st.text('OR')

text=st.text_area('Enter paragraph')

# Analyze button
if st.button('Analyze'):
    if article_url:
        # Parse the article
        article = Article(article_url)
        article.download()
        article.parse()
        doc = nlp(article.text)
    else:
        # Process the text from the text area
        doc = nlp(text)

    # Display the entities
    ent_html = displacy.render(doc, style="ent", jupyter=False)
    st.markdown(ent_html, unsafe_allow_html=True)