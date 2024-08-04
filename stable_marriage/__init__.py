from stable_marriage.candidate import Candidate
from stable_marriage.stable_marriage_algorithm import StableMarriageAlgorithm

MEN = [
    Candidate('A', ['Y', 'X', 'Z', 'W']),
    Candidate('B', ['Z', 'Y', 'W', 'X']),
    Candidate('C', ['X', 'W', 'Z', 'Y']),
    Candidate('D', ['Y', 'X', 'Z', 'W'])
]
WOMEN = [
    Candidate('W', ['B', 'A', 'D', 'C']),
    Candidate('X', ['C', 'D', 'B', 'A']),
    Candidate('Y', ['C', 'D', 'B', 'A']),
    Candidate('Z', ['A', 'C', 'B', 'D'])
]


def run_algo():
    print(StableMarriageAlgorithm.execute(MEN, WOMEN))
    print(StableMarriageAlgorithm.execute_simple(
        dict([(m.name, m.preferences) for m in MEN]),
        dict([(w.name, w.preferences) for w in WOMEN])
    ))


if __name__ == '__main__':
    run_algo()
