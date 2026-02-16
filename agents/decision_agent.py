#decision_agent
from config.ai_config import ACCEPTANCE_THRESHOLD

def decide(score: int) -> bool:
    return score >= ACCEPTANCE_THRESHOLD

