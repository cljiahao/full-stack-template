from sqlalchemy.orm import Session

from core.exceptions import InvalidInputError
from db.models.parent_example import ParentExample
from db.repository.parent_example import ParentExampleRepository


class ParentExampleService:
    def __init__(self, db: Session):
        """Initialize parent example service with parent example repository."""
        self.repo = ParentExampleRepository(db)

    def _validate_filter_conditions(self, filter_conditions: dict) -> None:
        """Validate filter conditions before querying or deleting."""
        if not filter_conditions:
            raise InvalidInputError("Filter conditions cannot be empty.")

    def _validate_lot_data(self, lot_data: dict):
        """Validate the lot data before creating."""
        if not lot_data:
            raise InvalidInputError("No data provided to create.")

    def _validate_update_data(self, update_data: dict):
        """Validate the update data before updating the record."""
        if not update_data:
            raise InvalidInputError("No data provided to update.")

    def create_parent_example(self, lot_data: dict) -> ParentExample:
        """Service layer method to create new parent example."""
        self._validate_lot_data(lot_data)

        return self.repo.create_parent_example(lot_data)

    def read_parent_example(self, filter_conditions: dict) -> ParentExample:
        """Service layer method to read parent example."""
        self._validate_filter_conditions(filter_conditions)

        return self.repo.read_parent_example(filter_conditions)

    def update_parent_example(
        self, filter_conditions: dict, update_data: dict
    ) -> ParentExample:
        """Service layer method to update parent example."""
        self._validate_filter_conditions(filter_conditions)
        self._validate_update_data(update_data)

        return self.repo.update_parent_example(filter_conditions, update_data)

    def delete_parent_example(self, filter_conditions: dict) -> ParentExample:
        """Service layer method to delete parent example."""
        self._validate_filter_conditions(filter_conditions)

        return self.repo.delete_parent_example(filter_conditions)
