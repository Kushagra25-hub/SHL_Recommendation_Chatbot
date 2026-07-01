class ConversationManager:
    """
    Responsible for deciding what the user wants.
    """

    def detect_intent(self, messages) -> str:
        """
        Detect intent using the entire conversation.
        """

        # Combine all USER messages
        conversation = " ".join(
            message["content"].lower()
            for message in messages
            if message["role"] == "user"
        )

        # Compare
        if "compare" in conversation:
            return "compare"

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

        if any(keyword in conversation for keyword in hiring_keywords):
            return "recommend"

        clarification_keywords = [
            "assessment",
            "test",
            "exam",
        ]

        if (
            len(conversation.split()) < 4
            and any(word in conversation for word in clarification_keywords)
        ):
            return "clarify"

        return "refuse"