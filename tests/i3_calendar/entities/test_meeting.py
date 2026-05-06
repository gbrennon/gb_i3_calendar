from datetime import datetime
import pytest

from i3_calendar.domain.entities import Meeting


class TestMeeting:
    @pytest.fixture
    def id(self) -> str:
        return "id"

    @pytest.fixture
    def title(self) -> str:
        return "Meeting Title"

    @pytest.fixture
    def start_at(self) -> datetime:
        return datetime.fromisoformat("2026-05-06 15:00:00")

    def test_title(self, id: str, start_at: datetime) -> None:
        title = "Foo"

        meeting = Meeting(id, title, start_at)

        expected_title = "Foo"
        assert expected_title == meeting.title

    def test_start_at(self, id: str, title: str) -> None:
        start_at = datetime.fromisoformat("2026-05-06 17:00:00")

        meeting = Meeting(id, title, start_at)

        expected_time = datetime.fromisoformat("2026-05-06 17:00:00")
        assert expected_time == meeting.start_at
