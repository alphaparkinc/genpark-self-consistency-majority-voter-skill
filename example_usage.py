from client import SelfConsistencyVoter

def main():
    print("=== Testing Self-Consistency Majority Voter ===")
    voter = SelfConsistencyVoter()

    sample_paths = [
        {"rationale": "Calculation via formula A", "answer": 120},
        {"rationale": "Calculation via formula B", "answer": 120},
        {"rationale": "Erroneous step at end", "answer": 110},
        {"rationale": "Direct estimation", "answer": 120},
        {"rationale": "Alternative geometric method", "answer": 120},
    ]

    consensus = voter.vote(sample_paths)
    print("Consensus Output:", consensus)
    assert consensus["consensus_answer"] == 120
    assert consensus["vote_count"] == 4
    assert consensus["confidence"] == 0.8
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
