from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agentic_ai.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraph_agentic_ai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraph_agentic_ai.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advance chatbot graph with tool integration.
        """
        # Define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)
        
        # Define the LLM
        llm = self.llm
        
        # Define the chatbot node
        obj_chatbot_with_node = ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        
        # Add Node
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        
        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
    
    def ai_news_builder_graph(self):
        """
        Builds AI news fetching and summarization graph.
        """
        ai_news_node = AINewsNode(self.llm)
        
        # Add nodes
        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result", ai_news_node.save_result)
        
        # Add edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_result")
        self.graph_builder.add_edge("save_result", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        Returns compiled graph for all usecases.
        """
        if usecase == 'Basic Chatbot':
            self.basic_chatbot_build_graph()
        elif usecase == 'Chatbot With Web':
            self.chatbot_with_tools_build_graph()
        elif usecase == 'AI News':
            self.ai_news_builder_graph()
        else:
            raise ValueError(f"Unknown usecase: {usecase}")
        
        # IMPORTANT: Return compiled graph for ALL usecases
        return self.graph_builder.compile()
