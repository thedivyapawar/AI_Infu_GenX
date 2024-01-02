import streamlit as st 
import app_component as au
from PIL import Image

st.set_page_config(
    page_title="AI InfuGenX- FAQ",
    page_icon="https://api.dicebear.com/5.x/bottts-neutral/svg?seed=faq"#,
)

st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

au.render_cta()

st.title("FAQ")

#st.markdown("---")
au.robo_avatar_component()

st.markdown("#### AI Designs")

with st.expander("What is AI InfuGenX?"):
    st.markdown("A ChatGPT clone is a replica or a similar version of the original ChatGPT language model . It is built using the same or similar deep learning architecture and training data as ChatGPT and is designed to simulate human-like conversations and respond to user input. ChatGPT clone script is a pre-built software that enables you to create a chatbot using the GPT model.")

with st.expander("What is GPT Clone?"):
    st.markdown("A ChatGPT clone is a replica or a similar version of the original ChatGPT language model . It is built using the same or similar deep learning architecture and training data as ChatGPT and is designed to simulate human-like conversations and respond to user input. ChatGPT clone script is a pre-built software that enables you to create a chatbot using the GPT model.")

with st.expander("What is GPT Shield?"):
    st.markdown(" GPT Shield AI Plagiarism Detector is streamlit app that gives you the perplexity and burstiness scores for LLM generated responses. It helps you detect some sort of plagiarism in the generated responses.")

with st.expander("What is Image AI?"):
    st.markdown("An AI-based image generation app built using Streamlit, Open AI's DALL-E.It is an app in which you can give any text prompt and it will create an image as per your prompt i.e will bring your imagination into reality.")

with st.expander("What is Music AI?"):
    st.markdown("Text to Music Generation App built using Meta's Audiocraft library. It is a Streamlit application utilises Music Gen small model.It works similarly as Image AI you have to enter the text prompt & it will create a background music based on the specified prompt.")

with st.expander("What language models do you support?"):
    st.markdown("""
    We currently support the following OpenAI models: gpt-3.5-turbo-16k, gpt-3.5-turbo, Dall_E, HuggingFace, and MusicGen,GPT-2-Tokenizer, LLM model . Each model has its own strengths and weaknesses, and the choice of model should be based on your specific use case. You can find detailed information on each model on https://platform.openai.com/docs/models and pricing information can be found on https://openai.com/api/pricing/.  \n
    """)

st.markdown("#### General")
with st.expander("What is OpenAI?"):
    st.markdown("OpenAI is an American artificial intelligence (AI) organization consisting of the non-profit OpenAI, registered in Delaware and its for-profit subsidiary corporation OpenAI Global, OpenAI researches artificial intelligence with the declared intention of developing safe and beneficial artificial general intelligence, which it defines as highly autonomous systems that outperform humans at most economically valuable work.")

with st.expander("What is an OpenAI API Key and why do I need one?"):
    st.markdown("An OpenAI API key is a unique credential that allows you to interact with OpeAI's GPT models. It also serves as your identifier in GPT Lab, allowing us to remember the AI Assistants you have created.")

with st.expander("How can I get an OpenAI API Key?"):
    st.markdown("You can obtain an OpenAI API Key by creating one on the OpenAI website: https://platform.openai.com/account/api-keys")

with st.expander("Why do I need to enter my OpenAI API key each time I use the app?"):
    st.markdown("For security reasons, your actual OpenAI Key is not stored on our servers. Our application only uses it during the duration of your sessions to interact with OpenAI. To keep track of your information, we use a secure one-way hashing algorithm to store a hashed version of your OpenAI API Key, which becomes your unique identifier in our backend data store. This helps ensure the confidentiality and security of your information.")

with st.expander("Does GPT cost money?"):
    st.markdown("Currently, GPT itself is free to use. However, you will incur costs for interacting with the OpenAI GPT models, as each API call to the model will be charged. The cost per call is relatively low, and under normal usage, the cost should be minimal. You have full control over the usage and cost of the model, as you are using your own API key. You can monitor your usage and costs through the OpenAI dashboard and adjust your usage accordingly to stay within your budget.")

with st.expander("Why am I getting a 'You exceeded your current quota, please check your plan and billing details.' error?"):
    st.markdown("This error typically indicates you have hit your maximum monthly spend (hard limit) for the API. However, you will likely see this error if you have a free trial API key. For optimal chatting experience, we recommend upgrading to a pay-as-you-go API key by entering your billing information [here](https://platform.openai.com/account/billing/overview). You can learn more about OpenAI API rate limits [here](https://platform.openai.com/docs/guides/rate-limits/overview).")

st.markdown("#### Privacy, Platform Guidelines, and Intellectual Property")

with st.expander("Is my information kept confidential on GPT_CLONE?"):
    st.markdown("Yes, we take your privacy and confidentiality very seriously. We do not store any personally identifiable information, and instead use a secure hashing algorithm to store a hashed version of your OpenAI API Key. Additionally, session transcripts are encrypted.")

with st.expander("Are there any restrictions on the type of models that can be created in OpenAI"):
    st.markdown("""
    Our Terms of Use have outlined some common sense restrictions you should follow. Please review our Terms of Use, available on the Terms page, for more information. 
    Additionally, since our AI Designs use the OpenAI language models, you should also comply with the [OpenAI Usage policies](https://platform.openai.com/docs/usage-policies).  \n
    Please note that (openai) does not assume any liability for the use of the AI DEsigns you create using the platform. It is your responsibility to ensure that your AI Designs complies with all applicable laws and regulations, and to use the platform at your own risk.
    """)

with st.expander("Who owns the prompts created in AI InfuGenX ?"):
    st.markdown("You do! The prompts created by the users in AI InfuGenX belong to the users themselves. Open AI is a platform that enables users to interact with and create their own AI Designs powered by OpenAI's language models, and the prompts created by the users in the app are the property of the users themselves.AI ConnectX does not claim any ownership or rights to the prompts created by the users.")

img=Image.open('logo.png')
st.sidebar.image(img)