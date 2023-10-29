__version__ = "1.0"

import streamlit as st
import openai
from wordcloud import WordCloud
from dotenv import load_dotenv
import os
import re
import json
import spacy
from spacy import displacy
from streamlit_chat import message
from bardapi import Bard
import torch
from diffusers import StableDiffusionPipeline

load_dotenv()

# Set up OpenAI API credentials
openai.api_key = "Your-OpenAI-API_key"

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


class HomePage:
    def __init__(self):
        pass

    def show(self):
        # st.title("Home")
        t1, t2, t3 = st.tabs(['🛖 Home', '📝 Terms', '🔐 **Privacy Policy**'])

        with t1:
            st.markdown("""# **Welcome to Vab AI – Where Imagination Meets Intelligence! 🚀**

Unlock the power of artificial intelligence with Vab AI, your one-stop destination for cutting-edge AI tools. We've curated a selection of the most frequently used AI tools and brought them together in one place to simplify your journey into the world of AI, Vab AI is your gateway to a universe of possibilities.

## 🔮 **Our AI Toolbox:**

### 1. **Text Analysis AI 📚**

Dive into the world of text analysis with our powerful tool that harnesses the OpenAI API. It offers a multitude of capabilities, including:

- 📌 **Name Entity Recognition**: Identify entities within text effortlessly.
- 🔑 **Key Binding**: Discover the keywords that matter the most.
- 🌟 **Most Positive Words**: Find the shining stars in your content.
- 📄 **Summary**: Get a concise summary of your text, making your life easier and more productive.

### 2. **Ask Me Anything 🤔**

Have a burning question? Our "Ask Me Anything" tool is powered by Google BERT and is ready to provide you with answers to any inquiry you throw its way. Simply ask, and let the AI work its magic to give you insightful responses in the blink of an eye. It's like having a digital oracle at your service! 🔮
                    
### 3. **Image Generation AI 📷**

Ever wanted to bring your imagination to life through art? Our Image Generation Model, powered by Hugging Face library, can turn your prompts into stunning visuals. Whether it's a vivid landscape, a unique character, or anything you can dream up, our AI brings it to reality ✨.

## 🌐 Vab AI Goes Big 🌐

We believe in the power of growth and innovation. While our first phase features incredible AI tools, we have bigger plans for the future:

**Phase Two: Training Our Own AI Models 🧠🤖**

We believe in continuous improvement. In our second phase, we're taking it up a notch. We're working on training our very own machine-learning models based on user interactions and feedback. This means even more customized, user-centric AI tools coming your way! 🚀📈

**Phase Three: A Full-Fledged AI Destination 🌐🚀**

Our journey doesn't stop here. In our final phase, we'll transform Vab AI into a full-fledged website. It will become your go-to hub for AI exploration, innovation, and interaction. Stay tuned for a seamless AI experience! 🌐💼

## **Open Source & Community-Powered** 💪

We believe in the power of community collaboration. Vab AI is an open-source project, and you're invited to contribute. Your input and ideas are always welcome! 

Visit our GitHub repository [here](https://github.com/vaibhav-kumawat/vab-ai) to see the magic happening behind the scenes. 💻🤝

Vab AI is more than a website; it's an evolving ecosystem of AI tools. Join us on this remarkable journey as we redefine the AI landscape. With Vab AI, the future is yours to create! 🌟💻🤖

Stay tuned for groundbreaking updates, and let Vab AI empower you like never before! 🔮🌠

                                        
""")

        with t2:
            st.markdown("""
        By using Vab AI and our AI tools, you agree to the following terms:

        ### 1. Use of AI Tools

        You may use our AI tools for personal and non-commercial purposes. Do not misuse the tools for harmful or malicious activities.

        ### 2. Ownership

        Vab AI retains ownership of the AI tools and any associated intellectual property.

        ### 3. Disclaimer

        While we strive for accuracy, we do not guarantee the correctness of the AI tool outputs. Use the tools at your own discretion.

        ### 4. Changes to the Terms and Privacy Policy

        We may update these terms and our privacy policy. Please review them periodically for any changes.

        ### 5. Contact Us

        If you have questions or concerns regarding this policy or our terms, you can reach us at vaibhav.kumawat017@gmail.com.

        Thank you for using Vab AI! We hope you find our AI tools useful in your endeavors.
    
    """)

        with t3:
            st.markdown("""
        Welcome to Vab AI! At Vab AI, we are committed to protecting your privacy and ensuring the security of your data. This Privacy Policy outlines how we collect, use, and protect your information when you use our website and the AI tools we offer.

        ### 1. Information We Collect

        When you use Vab AI, we may collect the following information:

        - **Personal Information:** Such as your name, email address, and other contact details provided during registration or communication with us.
        - **Usage Information:** We may collect information about how you interact with our AI tools, including your queries and interactions.
        - **AI Tool Data:** Any data you input into our AI tools for processing.

        ### 2. How We Use Your Information

        We use the information we collect for the following purposes:

        - To provide and improve our AI tools.
        - To respond to your queries and provide customer support.
        - To send you updates, promotional materials, and important information related to Vab AI.

        ### 3. Data Security

        We take data security seriously and implement appropriate measures to protect your information. We do not share your data with third parties without your consent.

        ### 4. Cookies and Tracking Technologies

        We may use cookies and tracking technologies to enhance your experience and provide analytics. You can control cookie preferences through your browser settings.

        ### 5. Third-Party Services

        Some of our AI tools use third-party services (e.g., Google Bard and OpenAI). Please refer to their privacy policies for how they handle your data.

        ### 6. Open Source and Contributions

        Vab AI is open source, and we welcome contributions from the community. If you'd like to contribute, you can find our GitHub repository [here](https://github.com/vab-ai).
    """)


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def generate_wordcloud(self):
        wordcloud = WordCloud(
            width=800, height=800, background_color="black", min_font_size=10
        ).generate(self.text)
        wordcloud.to_file("wordcloud.png")
        return "wordcloud.png"

    def ner(self):
        nlp = spacy.load("en_core_web_sm", disable=["parser", "tagger"])
        doc = nlp(self.text)
        html = displacy.render(doc, style="ent", jupyter=False)
        html = html.replace("\n\n", "\n")
        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)


class GPT3Analyzer(TextAnalyzer):
    def extract_key_findings(self):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Please find the key insights from the below text in maximum of 5 bullet points and also the summary in maximum of 3 sentences:\n"
            + self.text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response["choices"][0]["text"]

    def most_positive_words(self):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Please extract the most positive keywords from the below text\n"
            + self.text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response["choices"][0]["text"]


class AMA_AI:
    def __init__(self):
        os.environ[
            "_BARD_API_KEY"
        ] = "cAgxgwvTjpqcu7XtYv38_KSlBcwl25BSYS9ruz49Kw6C_N6dXXxEF-SohHhfASNcWqJFjQ."
        self.bard = Bard()
        self.generate = []
        self.past = []

    def response_api(self, prompt):
        response = self.bard.get_answer(str(prompt))["content"]
        return response

    def user_input(self):
        input_text = st.chat_input(placeholder="Enter Your Prompt:")
        return input_text

    def run(self):
        # st.title("Vab AI")
        user_text = self.user_input()

        if user_text:
            output = self.response_api(user_text)
            self.generate.append(output)
            self.past.append(user_text)

        if self.generate:
            for i in range(len(self.generate) - 1, -1, -1):
                message(self.past[i], is_user=True, key=str(i) + "_user")
                message(self.generate[i], key=str(i))


class ImageGenerator:
    def __init__(self):
        self.initialize_diffusion_pipeline()

    def initialize_diffusion_pipeline(self):
        try:
            if torch.cuda.is_available():
                self.pipe = StableDiffusionPipeline.from_pretrained(
                    "runwayml/stable-diffusion-v1-5", torch_device="cuda", torch_dtype=torch.float32)
            else:
                self.pipe = StableDiffusionPipeline.from_pretrained(
                    "runwayml/stable-diffusion-v1-5", torch_device="cpu", torch_dtype=torch.float32)
        except Exception as e:
            self.pipe = None
            st.error(
                f"An error occurred while initializing the Diffusion Pipeline: {str(e)}")

    def generate_image(self, text):
        try:
            if self.pipe is not None:
                prompt = text
                image = self.pipe(prompt).images[0]
                return image
            else:
                return None
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


# Streamlit Code
st.set_page_config(layout="wide")

# Add the provided code to the sidebar
st.sidebar.markdown(f"""
    # VabAI
    version {__version__} 
    
    All in one AI tool built with GPT3, BRAD AI & Hugging faces image gen libarary
    """)
st.sidebar.markdown("""
    Thank you for your interest in my application.
    Please be aware that this is only a Proof of Concept system
    and may contain bugs or unfinished features.
    If you like 👍🏻 this app you can [follow me](https://twitter.com/Vaibhav43491624)
    on Twitter for news and updates.
    """)
st.sidebar.markdown(
    'Source code can be found [here](https://github.com/vaibhavkumawat-17).')

# Sidebar navigation
selection = st.sidebar.radio("Select an option", [
                             "Home", "GPT3 Text Analyzer", "AMA AI", "Image Generation"])
st.title(selection)

# Initialize a variable for the selected page
selected_page = None

st.sidebar.markdown("""
    Made with ❤️ by [Vaibhav Kumawat](https://www.linkedin.com/in/vaibhav-kumawat017/).
    <br> Last Updated: October 29, 2023
                    """, unsafe_allow_html=True)

if selection == "Home":
    selected_page = HomePage()

elif selection == "GPT3 Text Analyzer":
    with st.expander("About GPT3 Text Analyzer"):
        st.markdown(
            "🔍 GPT3 Text Analyzer 📚 : Unleash the power of GPT-3 for supercharged text analysis and info extraction! 🚀")

    input_text = st.text_area("Enter your text to analyze")

    if input_text is not None:
        if st.button("Analyze Text"):
            analyzer = GPT3Analyzer(input_text)
            st.markdown("**Input Text**")
            st.info(input_text)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col1:
                st.markdown("**Key Findings based on your Text**")
                st.success(analyzer.extract_key_findings())
            with col2:
                st.markdown("**Output Text**")
                st.image(analyzer.generate_wordcloud())
            with col3:
                st.markdown("**Most Positive Words**")
                st.success(analyzer.most_positive_words())

            st.markdown("**Named Entity Recognition**")
            analyzer.ner()
elif selection == "AMA AI":
    with st.expander("About AMA AI"):
     st.markdown(
         "🤖 AMA AI 🤯 : Meet your new virtual buddy, AMA AI (Ask me aything AI), who's got your back with smart responses to your questions! 🙋‍♂️"
     )
    vab_ai = AMA_AI()
    vab_ai.run()

elif selection == "Image Generation":
    with st.expander("About Image Generation"):
        st.markdown(
            "🖼️ Image Generation 🌟 : Watch the magic happen with Huggingface Diffusers as they conjure up AI-powered images like never before! 🎨")

    # Create an instance of the ImageGenerator class
    image_generator = ImageGenerator()

    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt is not None:
        if st.button("Generate Image"):
            image_output = image_generator.generate_image(input_prompt)
            if image_output:
                st.info("Generating image.....")
                st.image(image_output,
                         caption="Generated by Huggingface Diffusers")

if selected_page:
    selected_page.show()

# Removing made with streamlit watermark from the bottom
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)