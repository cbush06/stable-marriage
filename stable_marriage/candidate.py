from typing import Optional


class Candidate:
    def __init__(self, name: str, preferences: list[str]):
        self._engaged_to = None
        self._name = name
        self._preferences = preferences

    @property
    def name(self) -> str:
        return self._name

    @property
    def current_preference(self) -> str:
        return self._preferences[0]

    @property
    def preferences(self) -> list[str]:
        return self._preferences

    @property
    def engaged_to(self) -> str:
        return self._engaged_to

    @engaged_to.setter
    def engaged_to(self, value: str) -> None:
        self._engaged_to = value

    @property
    def is_free(self) -> bool:
        return self._engaged_to is None

    def propose(self, candidates: list[str]) -> Optional[str]:
        if not candidates:
            return None

        # Select the highest ranking candidate from the list
        selection: Optional[str] = self._engaged_to
        for candidate in candidates:  # For each suitor
            if (selection is None  # And he is the first candidate
                    or self._preferences.index(candidate) < self._preferences.index(
                        selection)):  # Or he is higher ranked than the current selection
                selection = candidate

        return selection

    def accept(self, candidate: str) -> None:
        self._engaged_to = candidate  # Engage with the new partner

    def reject_by(self, candidate: str) -> None:
        self._preferences.remove(candidate) # Remove the candidate from the preference list
        pass

    def jilt(self) -> None:
        self.reject_by(self._engaged_to)
        self._engaged_to = None  # Break up with the current partner
