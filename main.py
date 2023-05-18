import streamlit as st
import requests

api_key = "xxxxxxxxxxxxxxxxxx" #your api key 
url = "https://api.nasa.gov/planetary/apod?api_key=xxxxxxxxxxxxxxxx"

response = requests.get(url)
content = response.json()
image = content['url']
explanation = content['explanation']
title = content['title']

st.title(title)
st.image(image)
st.write(explanation)


