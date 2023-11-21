import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import matplotlib.pyplot as plt

load_dotenv()

#openai_api_key = os.getenv("OPENAI_API_KEY")
#os.environ["OPENAI_API_KEY"] = "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"

# make the GUI
st.set_page_config(
    layout="centered",
    page_title="Intelligent_QA",
    page_icon=":question:",
)

# st.title("Intelligent Analysis over Multiple CSVs")
st.markdown(
    "<h1 style='font-size: 35px; color: Slateblue;'>Intelligent Analysis over Multiple CSVs</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h1 style='font-size: 20px; color: red;'>Question and Answer Over Multiple CSV Files</h1>",
    unsafe_allow_html=True,
)

def query_agent(df, prompt):
    """
    Query an agent and return the response as a string.
    Args:
        agent: The agent to query.
        query: The query to ask the agent.
    Returns:
        The response from the agent as a string.
    """
    llm = OpenAI()
    # agent - takes csv file path, returns an agent that can access and use LLM
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agent.run(prompt)

# Load CSVs
input_csvs = st.file_uploader(
    "Upload your CSVs for analysis",
    type=["csv"],
    accept_multiple_files=True,
)

if input_csvs:
    select_file = st.selectbox(
        "Select a CSV", [files.name for files in input_csvs]
    )
    selected_index = [files.name for files in input_csvs].index(select_file)

    st.markdown(
        "<h1 style='font-size: 17px; color: Slateblue;'>CSV Files Uploaded Successfully</h1>",
        unsafe_allow_html=True,
    )
    data = pd.read_csv(input_csvs[selected_index])
    st.dataframe(data, use_container_width=True)

    st.markdown(
        "<h1 style='font-size: 20px; color: Slateblue;'>Chat Below</h1>",
        unsafe_allow_html=True,
    )
    input_text = st.text_area("Enter the query")
    if input_text:
        if st.button("Submit Query"):
            result = query_agent(data, input_text)
            st.success(result, icon="✅")





def random_function():
    pass

