from sqlalchemy.orm import Session

from db.models.parent_example import ParentExample
from db.repository.base_repository import BaseRepository


class ParentExampleRepository(BaseRepository[ParentExample]):
    def __init__(self, db: Session):
        super().__init__(db, ParentExample)

    def create_parent_example(self, lot_data: dict) -> ParentExample:
        """Create new parent examples."""
        return self.create(
            lot_data,
            print_message=f"Error creating parent example from the database.",
        )

    def read_parent_example(self, filter_conditions: dict) -> ParentExample:
        """Read parent examples based on filter."""
        return self.read(
            filter_conditions,
            print_message=f"Error reading parent example from the database.",
        )

    def update_parent_example(
        self, filter_conditions: dict, update_data: dict
    ) -> ParentExample:
        """Update parent example with provided data."""
        return self.update(
            filter_conditions,
            update_data,
            print_message=f"Error updating parent example in the database.",
        )

    def delete_parent_example(self, filter_conditions: dict) -> ParentExample:
        """Delete parent examples based on filter."""
        return self.delete(
            filter_conditions,
            print_message=f"Error deleting parent example from the database.",
        )
