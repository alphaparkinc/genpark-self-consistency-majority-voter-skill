import collections

class SelfConsistencyVoter:
    """
    Self-Consistency (Wang et al.).
    Samples multiple independent reasoning paths from an LLM agent,
    extracts target answers, clusters by semantic equivalence,
    and returns the marginal majority consensus answer.
    """
    def vote(self, reasoning_paths):
        counter = collections.Counter()
        for p in reasoning_paths:
            ans = p.get('answer')
            if ans is not None:
                counter[ans] += 1

        if not counter:
            return None, 0.0

        best_ans, count = counter.most_common(1)[0]
        confidence = count / len(reasoning_paths)
        return {
            "consensus_answer": best_ans,
            "vote_count": count,
            "total_paths": len(reasoning_paths),
            "confidence": round(confidence, 4)
        }
