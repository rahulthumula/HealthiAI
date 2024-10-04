import streamlit as st
from multimodelgemini import BillBuddy

# Initialize BillBuddy
bill_buddy = BillBuddy()

# Set up the Streamlit app
st.title("BillBuddy: Your Financial Assistant")

# Sidebar for uploading files
uploaded_file = st.sidebar.file_uploader("Upload your expense file", type=["csv", "pdf", "txt"])

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process file if uploaded
    if uploaded_file is not None:
        analysis_results = bill_buddy.process_file(uploaded_file.name)
        st.session_state.messages.append({"role": "assistant", "content": str(analysis_results)})
        with st.chat_message("assistant"):
            st.markdown(str(analysis_results))

    # Generate and display bot's response
    response = bill_buddy.generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    # Generate a recommendation and display it
    recommendation = bill_buddy.recommend_question()
    st.session_state.messages.append({"role": "assistant", "content": recommendation})
    with st.chat_message("assistant"):
        st.markdown(recommendation)