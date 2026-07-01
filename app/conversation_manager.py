class ConversationManager:
    """
    Responsible for deciding what the user wants.
    """

    def detect_intent(self, messages) -> str:
        """
        Detect the user's intent based on the latest message.
        """

        latest_message = messages[-1]["content"].lower()

        # Compare intent
        if "compare" in latest_message:
            return "compare"

        # Hiring / recommendation intent
        hiring_keywords = [
            "hire",
            "hiring",
            "looking",
            "need",
            "recruit",
            "candidate",
            "developer",
            "engineer",
            "analyst",
            "manager",
            "sales",
            "support",
            "intern",
            "graduate",
            "assessment",
            "test",
        ]

        if any(keyword in latest_message for keyword in hiring_keywords):
            return "recommend"

        # Clarification only for vague assessment requests
        clarification_keywords = [
            "assessment",
            "test",
            "exam",
        ]

        if (
            len(latest_message.split()) < 4
            and any(word in latest_message for word in clarification_keywords)
        ):
            return "clarify"

        # Everything else
        return "refuse"


if __name__ == "__main__":
    manager = ConversationManager()

    test_messages = [
        "Looking for a Python developer",
        "Compare OPQ32 and GSA",
        "Assessment",
        "Weather today?"
    ]

    for message in test_messages:
        result = manager.detect_intent([
            {
                "role": "user",
                "content": message
            }
        ])
        print(f"{message} --> {result}")