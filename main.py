import streamlit as st
import requests

api_key = "MTuKmw2YnTvugrFgBrVCa3eKMxpvblU5W1EqoEi8"
url = "https://api.nasa.gov/planetary/apod?api_key=MTuKmw2YnTvugrFgBrVCa3eKMxpvblU5W1EqoEi8"

response = requests.get(url)
content = response.json()
image = content['url']
explanation = content['explanation']
title = content['title']

st.title(title)
st.image(image)
st.write(explanation)


