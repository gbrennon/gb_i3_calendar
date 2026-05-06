from datetime import datetime

from forging_blocks.domain import Entity


class Meeting(Entity[str]):
    def __init__(self, id: str, title: str, start_at: datetime) -> None:
        self._title = title
        self._start_at = start_at
        super().__init__(id)

    @property
    def title(self) -> str:
        return self._title

    @property
    def start_at(self) -> datetime:
        return self._start_at
