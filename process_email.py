import os
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from email_state import EmailState
from llm_gemini import LLM_Gemini

# Initialize our LLM
model = LLM_Gemini()

def read_email(state: EmailState):
    """Alfred reads and logs the incoming email"""
    email = state["email"]
    
    # Here we might do some initial preprocessing
    print(f"Alfred is processing an email from {email['sender']} with subject: {email['subject']}")
    
    # No state changes needed here
    return {}

def classify_email(state: EmailState):
    """Alfred uses an LLM to determine if the email is spam or legitimate"""
    email = state["email"]
    
    # Prepare our prompt for the LLM
    prompt = f"""
    As Alfred the butler, analyze this email and determine if it is spam or legitimate.
    
    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}
    
    First, determine if this email is spam. If it is spam, explain why, and start your explanation with indicator "reason:"
    If it is legitimate, categorize it (inquiry, complaint, thank you, etc.).
    """
        # Call the LLM
    response = model.chat(prompt = prompt)
    
    # Simple logic to parse the response (in a real app, you'd want more robust parsing)
    response_text = response.lower()
    is_spam = "spam" in response_text and "not spam" not in response_text
    
    # Extract a reason if it's spam
    spam_reason = None
    # Determine category if legitimate
    email_category = None
    if is_spam and "reason:" in response_text:
        spam_reason = response_text.split("reason:")[1].strip()
    else:
        if not is_spam:
            categories = ["inquiry", "complaint", "thank you", "request", "information"]
            for category in categories:
                if category in response_text:
                    email_category = category
                    break
        
    # Update messages for tracking
    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ]
    
    # Return state updates
    return {
        "is_spam": is_spam,
        "spam_reason": spam_reason,
        "email_category": email_category,
        "messages": new_messages
    }

def handle_spam(state: EmailState):
    """Agent discards spam email with a note"""
    print(f"Agent has marked the email as spam. Reason: {state['spam_reason']}")
    print("The email has been moved to the spam folder.")
    
    # We're done processing this email
    return {}

def draft_response(state: EmailState):
    """The agent drafts a preliminary response for legitimate emails"""
    email = state["email"]
    category = state["email_category"] or "general"
    
    # Prepare our prompt for the LLM
    prompt = f"""
    As the agent the butler, draft a polite preliminary response to this email.
    
    Email:
    From: {email['sender']}
    Subject: {email['subject']}
    Body: {email['body']}
    
    This email has been categorized as: {category}
    
    Draft a brief, professional response that Mr. xxx can review and personalize before sending.
    """
    
    # Call the LLM
    response = model.chat(prompt = prompt)
    
    # Update messages for tracking
    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response}
    ]
    
    # Return state updates
    return {
        "email_draft": response,
        "messages": new_messages
    }

def notify_mr_xxx(state: EmailState):
    """Agent notifies Mr. xxx about the mail and provides a draft response to review and respond"""
    email = state["email"]
    
    print("\n" + "="*50)
    print(f"Sir, you've received an email from {email['sender']}.")
    print(f"Subject: {email['subject']}")
    print(f"Category: {state['email_category']}")
    print("\nI've prepared a draft response for your review:")
    print("-"*50)
    print(state["email_draft"])
    print("="*50 + "\n")
    
    # We're done processing this email
    return {}

def route_email(state: EmailState) -> str:
        ##"""Determine the next step based on spam classification"""
        if state["is_spam"]:
            return "spam"
        else:
            return "legitimate"