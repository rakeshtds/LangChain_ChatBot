import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="AD | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):



#Title
st.markdown(
    """
    <h2 style='text-align: center;'>AD, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description


#AD's Pages
st.subheader("🚀 AD's Pages")
st.write("""
- **AD-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore]
- **AD-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent]

""")
st.markdown("---")


#Contributing






