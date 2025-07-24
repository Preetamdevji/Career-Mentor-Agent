class IntentAgent:
    def __init__(self) -> None:
        pass

    def detect_intent(self, user_input: str) -> dict:
        
        user_input = user_input.lower()
        if "career" in user_input:
            return {
                "target_agent": "CareerAgent",
                "reason": "User is asking about career options.",
                "confidence": 0.9
            }
        elif "skill" in user_input or "prepare" in user_input:
            return {
                "target_agent": "SkillAgent",
                "reason": "User is asking about skill roadmap.",
                "confidence": 0.9
            }
        elif "job" in user_input:
            return {
                "target_agent": "JobAgent",
                "reason": "User is asking about job roles.",
                "confidence": 0.9
            }
        else:
            return {
                "target_agent": "CareerAgent",
                "reason": "Fallback to CareerAgent by default.",
                "confidence": 0.5
            }
        
