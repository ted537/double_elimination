"""
The Participant class represents a participant in a specific match.
It can be used as a placeholder until the participant is decided.
"""

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Participant(Generic[T]):
    """
    The Participant class represents a participant in a specific match.
    It can be used as a placeholder until the participant is decided.
    """
    def __init__(self, competitor=None):
        self.competitor = competitor

    def __repr__(self) -> str:
        return f'<Participant {self.competitor}>'

    def get_competitor(self) -> Optional[T]:
        """
        Return the competitor that was set,
        or None if it hasn't been decided yet
        """
        return self.competitor

    def set_competitor(self, competitor: T) -> None:
        """
        Set competitor after you've decided who it will be,
        after a previous match is completed.
        """
        self.competitor = competitor
