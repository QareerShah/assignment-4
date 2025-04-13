import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(page_title="My Streamlit App", page_icon="🛡️", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
    }
    footer {
        visibility: hidden;
    }
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_mjlh3hcy.json")

# App title
st.title("🚀 Welcome to My Streamlit App!")

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Choose a page", ["🏠 Home", "ℹ️ About", "📞 Contact"])

# Home Page
if page.startswith("🏠"):
    st.header("🏠 Home Page")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("home-page.svg")
    with col2:
        st.write("This is the **Home Page** of the app — built with Python and Streamlit!")
        name = st.text_input("👤 Enter your name:", placeholder="e.g., Your Name")
        if name:
            st.success(f"👋 Hello, {name}!")
        else:
            st.info("Please enter your name above to get greeted.")

    st_lottie(lottie_hello, height=200)

# About Page
elif page.startswith("ℹ️"):
    st.header("ℹ️ About Page")
    st.write("""
    Welcome to the **About Page**!  
    This app is built with ❤️ using [Streamlit](https://streamlit.io/).  
    It's a simple demo showcasing page navigation, animations, user input, and clean design.
    """)
    st.image("about-page.svg", width=500)

# Contact Page
elif page.startswith("📞"):
    st.header("📞 Contact Page")
    st.write("Got a message? We'd love to hear from you!")

    email = st.text_input("📧 Enter your email:", placeholder="you@example.com")
    message = st.text_area("💬 Your message:", placeholder="Type your message here...")

    if st.button("Submit"):
        if email and message:
            st.success("✅ Thank you! We've received your message and will get back to you soon.")
        else:
            st.warning("⚠️ Please enter both email and message.")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit by <b>Your Name</b></center>", unsafe_allow_html=True)
