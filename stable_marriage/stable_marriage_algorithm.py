from functools import reduce
from typing import Optional

from stable_marriage import Candidate


class StableMarriageAlgorithm:

    @staticmethod
    def execute(men: list[Candidate], women: list[Candidate]) -> list[tuple[str, str]]:
        free_men = len(men)
        men_map = dict([(m.name, m) for m in men])

        while free_men > 0:
            proposition_map: dict[str, list[str]] = dict([(w.name, []) for w in women])

            # Assign a list of suitors to each woman
            for m in men:
                if m.is_free and m.current_preference is not None:
                    proposition_map[m.current_preference].append(m.name)

            # Propose each list to each woman
            for w in women:
                decision = w.propose(proposition_map[w.name])
                if decision is not None and decision != w.engaged_to:
                    if w.engaged_to is not None:
                        men_map[w.engaged_to].jilt()
                    w.engaged_to = decision
                    men_map[decision].accept(w.name)

                # Reject all failed suitors
                [men_map[m].reject_by(w.name) for m in filter(lambda m: m != decision, proposition_map[w.name])]

            free_men = reduce(lambda free, m: free + 1 if m.is_free else free, men, 0)

        return [(m.name, m.engaged_to) for m in men]

    @staticmethod
    def execute_simple(men: dict[str, list[str]], women: dict[str, list[str]]):
        free_men: list[str] = list(men.keys())
        engagements: dict[str, Optional[str]] = dict([(name, None) for name in list(men.keys()) + list(women.keys())])

        while free_men:
            for m in free_men:
                prefs = men[m]
                next_pref = prefs.pop(0)

                if engagements[next_pref] is None:
                    engagements[next_pref] = m
                    engagements[m] = next_pref
                elif women[next_pref].index(m) < women[next_pref].index(engagements[next_pref]):
                    engagements[engagements[next_pref]] = None
                    engagements[next_pref] = m
                    engagements[m] = next_pref

            free_men = [m for m in filter(lambda name: engagements[name] is None, men.keys())]

        print(engagements)