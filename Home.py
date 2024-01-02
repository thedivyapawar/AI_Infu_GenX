import streamlit as st
import json
import requests 
from streamlit_lottie import st_lottie 
from PIL import Image

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/
st.set_page_config(
    layout="wide",
    page_icon= "🤖",
    page_title= "InfuGenX"
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("lottiefiles/chatbot.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

st.title("      WELCOME TO :blue[AI InfuGenX]       ")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=None,
    width=None,
    key=None,
)

st.subheader(":blue[AI InfuGenX] is an :blue[streamlit app] integrated with some of the :blue[OpenAI] functionalities.")
st.write("⚙  :red[WORKING MODEL] ")
st.write("💡 STEP 1 ")
lottie_robot = load_lottiefile("lottiefiles/robotworking.json")
st_lottie(
    lottie_robot,
)

st.write("💡 STEP 2 ")
lottie_working = load_lottiefile("lottiefiles/workingmodel.json")
st_lottie(
    lottie_working,
)

st.write("💡 STEP 3 ")
lottie_workingmodel = load_lottiefile("lottiefiles/coding.json")
st_lottie(
    lottie_workingmodel,
)

img=Image.open('logo.png')
st.sidebar.image(img)