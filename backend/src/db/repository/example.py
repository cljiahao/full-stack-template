from sqlalchemy.orm import Session

from db.models.example import Example
from db.repository.base_repository import BaseRepository


class ExampleRepository(BaseRepository[Example]):
    def __init__(self, db: Session):
        super().__init__(db, Example)
        self.db = db

    def create_bulk_example(self, bulk_example: list[dict]) -> list[Example]:
        """Create new example."""
        return self.create(
            bulk_example,
            print_message=f"Error creating example into the database.",
        )

    def read_all_example(self, filter_conditions: dict) -> list[Example]:
        """Read example based on filter."""
        return self.read(
            filter_conditions,
            return_all=True,
            print_message=f"Error reading example from the database.",
        )

    def update_bulk_example(
        self, filter_conditions: list[dict], update_data: list[dict]
    ) -> int:
        """Update example with provided data."""
        return self.update(
            filter_conditions,
            update_data,
            print_message=f"Error updating example in the database.",
        )

    def delete_bulk_example(self, filter_conditions: list[dict]) -> int:
        """Update example with provided data."""
        return self.delete(
            filter_conditions,
            print_message=f"Error deleting example from the database.",
        )
