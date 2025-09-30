from process_feedback import compiled_graph

# Example +ve
positive_fedback = {
    "sender": "user1",
    "feedback": "Your product is excellent. I love its ease of usability",
}

# Example -ve
negative_feedback = {
    "sender": "user2",
    "feedback": "Your product is awful. its frustrating to use your product and difficult to use",
}

# Example neutral
neutral_feedback = {
    "sender": "user3",
    "feedback": "Your product is ok. I am ok to use but not finding any great feature to refer to friends",
}

# Process the +ve
print("\nProcessing legitimate email...")
legitimate_result = compiled_graph.invoke({
    "feedback": positive_fedback,
    "feedback_category": None,
    "feedback_summary": None,
    "star_rating": None,
    "messages": []
})

# Process the neutral
print("\nProcessing legitimate email...")
legitimate_result = compiled_graph.invoke({
    "feedback": neutral_feedback,
    "feedback_category": None,
    "feedback_summary": None,
    "star_rating": None,
    "messages": []
})

# Process the -ve
print("\nProcessing legitimate email...")
legitimate_result = compiled_graph.invoke({
    "feedback": negative_feedback,
    "feedback_category": None,
    "feedback_summary": None,
    "star_rating": None,
    "messages": []
})

