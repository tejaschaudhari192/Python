import streamlit as st
import requests

api_url = "https://api.shrtco.de/v2/shorten"


st.header('Teja\'s URL Shortner')
user_link = st.text_input("enter link")
if st.button("Shorten"):
    param = {"url": user_link}
    response = requests.get(url=api_url, params=param)
    all = response.json()
    # print(all)
    print(response.status_code)
    try:
        shrt2 = all["result"]["short_link2"]
    except:
        st.warning("invalid URL")
    else:
        st.write('Shortned URL : ')
        st.text(shrt2)

