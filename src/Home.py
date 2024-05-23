import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Robby | Chat-Bot 🤖")



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>AD, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

#Contact
with st.sidebar.expander("📬 Contact"):



#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'> intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Robby's Pages")
st.write("""
- **Robby-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore]
- **Robby-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent]
""")
st.markdown("---")

