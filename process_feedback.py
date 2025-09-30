from feedback_state import FeedbackState
from langgraph.graph import StateGraph, START, END
from feedback_analyzer import read_feedback, classify_feedback

# Create the graph
feedback_graph = StateGraph(FeedbackState)

# Add nodes
feedback_graph.add_node("read_feedback", read_feedback)
feedback_graph.add_node("classify_feedback", classify_feedback)

# Start the edges
feedback_graph.add_edge(START, "read_feedback")
# Add edges - defining the flow
feedback_graph.add_edge("read_feedback", "classify_feedback")

feedback_graph.add_edge("classify_feedback", END)

# Compile the graph
compiled_graph = feedback_graph.compile()