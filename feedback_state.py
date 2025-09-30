import os
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage

class FeedbackState(TypedDict):
    # The feedback being processed
    feedback: Dict[str, Any]  # Contains sender, feedback.

    # +ve or -ve feedback
    feedback_category: Optional[str]

    # feedback summary
    feedback_summary: Optional[str]

    # Rating generated as per the feedback shared, generated automatically if the  client has not shared in the feedback
    star_rating: Optional[str]

    # Processing metadata
    messages: List[Dict[str, Any]]  # Track conversation with LLM for analysis