from career_mentor_agent.src.career_mentor_agent.agents.career_agent import CareerAgent
from career_mentor_agent.src.career_mentor_agent.agents.intent_agent import IntentAgent
from career_mentor_agent.src.career_mentor_agent.agents.job_agent import JobAgent
from career_mentor_agent.src.career_mentor_agent.agents.skill_agent import SkillAgent


class MentorAgent:
    def __init__(self):
        self.intent_agent=IntentAgent()
        self.career_agent=CareerAgent()
        self.skill_agent=SkillAgent()
        self.job_agent=JobAgent()

    async def handle_input(self, user_input):
        intent = self.intent_agent.detect_intent(user_input)
        if intent == 'career':
            return await self.career_agent.suggest_careers(user_input)
        elif intent == "skill":
            return await self.skill_agent.get_skill_roadmap(user_input)
        elif intent == "job":
            return await self.job_agent.suggest_jobs(user_input)
        else:
            return "Sorry, I didn't understand. Please ask about career, skills, or jobs."