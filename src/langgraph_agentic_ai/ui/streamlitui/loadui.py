import streamlit as st
import os
from dotenv import load_dotenv
from src.langgraph_agentic_ai.ui.uiconfigfile import Config

# Load environment variables from .env file
load_dotenv()

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            # get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected llm"] = st.selectbox("Selected LLM", llm_options)

            if self.user_controls["selected llm"] == "Groq":
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                
                # Initialize session state with env variable if not exists
                if "GROQ_API_KEY" not in st.session_state:
                    st.session_state["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
                
                # Use key parameter - Streamlit handles session state automatically
                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "API key",
                    value=st.session_state["GROQ_API_KEY"],
                    key="groq_input",
                    type="password"
                )
                
                # validate api key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API KEY to proceed")

            # usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot With Web" or self.user_controls['selected_usecase'] == "AI News":
                # Initialize session state with env variable if not exists
                if "TAVILY_API_KEY" not in st.session_state:
                    st.session_state["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", "")
                
                # Use key parameter - Streamlit handles session state automatically
                self.user_controls["TAVILY_API_KEY"] = st.text_input(
                    "TAVILY API KEY",
                    value=st.session_state["TAVILY_API_KEY"],
                    key="tavily_input",
                    type="password"
                )
                
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"]
    
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY API KEY to proceed. don't have ? proceed here: [http://tavily.com/](http://tavily.com/) ")

            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("🤖 AI News Explorer ")
                with st.sidebar:
                    time_frame = st.selectbox(
                        "🗓️ Select Time Frame",
                        ["Daily", "Monthly", "Weekly"],
                        index=0
                    )
                if st.button("🔎 Fetch Latest AI News", use_container_width=True):
                    st.session_state.timeframe = time_frame
                    st.session_state.IsFetchButtonClicked = True
                    
        return self.user_controls
