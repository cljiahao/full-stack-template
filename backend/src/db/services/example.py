from sqlalchemy.orm import Session

from core.exceptions import InvalidInputError
from db.models.example import Example
from db.repository.example import ExampleRepository


class ExampleService:
    def __init__(self, db: Session):
        """Initialize example service with example repository."""
        self.repo = ExampleRepository(db)

    def _validate_filter_conditions(self, filter_conditions: dict) -> None:
        """Validate filter conditions before querying or deleting."""
        if not filter_conditions:
            raise InvalidInputError("Filter conditions cannot be empty.")

    def _validate_update_data(self, update_data: dict):
        """Validate the update data before updating the record."""
        if not update_data:
            raise InvalidInputError("No data provided to update.")

    def create_example(self, example_data: list[dict]) -> list[Example]:
        """Service layer method to create new example."""

        return self.repo.create_bulk_example(example_data)

    def read_example(self, filter_conditions: dict) -> list[Example]:
        """Service layer method to read example."""
        self._validate_filter_conditions(filter_conditions)

        return self.repo.read_all_example(filter_conditions)

    def update_example(
        self, filter_conditions: list[dict], update_data: list[dict]
    ) -> int:
        """Service layer method to update example."""
        for filters in filter_conditions:
            self._validate_filter_conditions(filters)
        for updates in update_data:
            self._validate_update_data(updates)

        return self.repo.update_bulk_example(filter_conditions, update_data)

    def delete_example(self, filter_conditions: list[dict]) -> int:
        """Service layer method to delete example."""
        for filters in filter_conditions:
            self._validate_filter_conditions(filters)

        return self.repo.delete_bulk_example(filter_conditions)
