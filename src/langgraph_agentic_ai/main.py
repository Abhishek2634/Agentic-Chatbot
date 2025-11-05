import streamlit as st
from src.langgraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMS.groqllm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI applications with Streamlit UI
    """
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("ERROR: Failed to load user input from the UI")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return

            # Initialize and setup the graph based on usecase
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No usecase selected.")
                return

            # Graph builder
            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                
                # Verify graph was compiled successfully
                if graph is None:
                    st.error("Error: Graph setup returned None.")
                    return
                
                if not hasattr(graph, 'stream'):
                    st.error("Error: Graph is not properly compiled.")
                    return
                
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
                
            except ValueError as e:
                st.error(f"Error: {e}")
                return
            except AttributeError as e:
                st.error(f"Error: Graph attribute error. {e}")
                return
            except Exception as e:
                st.error(f"Error: Graph setup failed. {e}")
                return

        except Exception as e:
            st.error(f"Application error: {e}")
            return


if __name__ == "__main__":
    load_langgraph_agenticai_app()
