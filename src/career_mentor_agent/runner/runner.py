from career_mentor_agent.career_agent import CareerAgent
from career_mentor_agent.intent_agent import IntentAgent
from career_mentor_agent.job_agent import JobAgent
from career_mentor_agent.skill_agent import SkillAgent


class Runner:
    def __init__(self) -> None:
        # Agent Initialize
        self.intent_agent = IntentAgent()
        self.agent_map = {
            "CareerAgent": CareerAgent(),
            "SkillAgent": SkillAgent(),
            "JobAgent": JobAgent()
        }

        self.context = {}       #For storing user state if needed later

    def run(self, user_input: str):
        intent_result = self.intent_agent.detect_intent(user_input)
        target_agent_name = intent_result["target_agent"]

        target_agent = self.agent_map[target_agent_name]
        response = target_agent.run(user_input)

        return {
            "agent": target_agent_name,
            "response": response,
            "metadata": {
                "handoff_reason": intent_result["reason"],
                "confidence": intent_result["confidence"] 
            }
        }
