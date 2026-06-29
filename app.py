import streamlit as st
from main import chat

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Currency Converter",
    page_icon="💱",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------

st.markdown("""
<style>

.main {
    background-color: #F8F9FA;
}

h1 {
    color: #2E8B57;
}

div[data-testid="stSidebar"] {
    background-color: #F1F3F6;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("💱 Currency Agent")

    st.markdown("---")

    st.write("### Technologies")

    st.success("✅ Python")

    st.success("✅ Streamlit")

    st.success("✅ OpenRouter")

    st.success("✅ Exchange Rate API")

    st.markdown("---")

    st.write("### Example Questions")

    st.info("Convert 100 USD to INR")

    st.info("Convert 500 INR to EUR")

    st.info("Convert 50 GBP to USD")

    st.info("How much is 1000 JPY in INR?")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# -------------------------------
# Main Page
# -------------------------------

st.title("💱 AI Currency Converter Agent")

st.write(
    "Ask me to convert currencies using natural language."
)

# -------------------------------
# Chat History
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -------------------------------
# Chat Input
# -------------------------------

prompt = st.chat_input(
    "Type your currency conversion request..."
)

if prompt:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # AI Response
    with st.spinner("Converting currency..."):

        try:

            response = chat(prompt)

        except Exception as e:

            response = f"❌ Error: {e}"

    with st.chat_message("assistant"):

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )