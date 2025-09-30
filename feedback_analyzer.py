import os, json, re
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from feedback_state import FeedbackState
from llm_gemini import LLM_Gemini
from logger import get_logger

# Initialize our LLM
model = LLM_Gemini()
logger = get_logger("feedback_analyzer")

def read_feedback(state: FeedbackState):
    """The agent reads and logs the incoming feeback from the client"""
    feedback = state["feedback"]
    
    # Here we might do some initial preprocessing
    logger.info(f"Agent is analying the feedback from {feedback['sender']}. Feedback: {feedback['feedback']}")
    
    # No state changes needed here
    return {}

def classify_feedback(state: FeedbackState):
    """Agent uses an LLM to determine if the feedback is +ve or -ve or neutral"""
    feedback = state["feedback"]
    
    # Prepare our prompt for the LLM
    prompt = f'''
        As the agent, analyze this feedback and determine if the feedback is +ve, -ve or neutral.
        
        From: {feedback['sender']}
        feedback: {feedback['feedback']}
        
        determine if this feedback is positive or negative or neutral 
        Provide the response the format

                "feedback_category": "+ve or -ve or neutral",
                "feedback_summary": "a breif summary of the feedback",
                "star_rating": "if client has not provided the star rating, derive based on the feedback"
        '''
        # Call the LLM
    response = model.chat(prompt = prompt)

    match = re.findall(r'\{.*?\}', response, re.DOTALL)
    if match:
        json_str = match[0]
        feedback_data = json.loads(json_str)
        print(feedback_data)
    else:
        print("No JSON found in message.")

    feedback_category = feedback_data["feedback_category"]
    feedback_summary = feedback_data["feedback_summary"]
    star_rating = feedback_data["star_rating"]

    logger.info(f"""
        Here is the feedback summary : 

        feedback: {feedback}
        feedback_category: {feedback_category}
        feedback_summary: {feedback_summary}
        star_rating: {star_rating}

    """)

    # Update messages for tracking
    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ]
    
    # Return state updates
    return {
        "feedback": feedback,
        "feedback_category": feedback_category,
        "feedback_summary": feedback_summary,
        "star_rating": star_rating,
        "messages": new_messages
    }
