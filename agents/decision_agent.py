from config.ai_config import ACCEPTANCE_THRESHOLD

def decide(score: float) -> dict:

    accepted = score >= ACCEPTANCE_THRESHOLD

    if accepted:
        reason = (
            f"Accepted: score {score} meets or exceeds "
            f"threshold {ACCEPTANCE_THRESHOLD}"
        )
    else:
        reason = (
            f"Rejected: score {score} below "
            f"threshold {ACCEPTANCE_THRESHOLD}"
        )

    return {
        "accepted": accepted,
        "score": score,
        "threshold": ACCEPTANCE_THRESHOLD,
        "reason": reason
    }
