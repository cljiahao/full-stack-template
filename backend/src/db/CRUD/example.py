from sqlalchemy import select
from sqlalchemy.orm.session import Session

from db.models.example import EXAMPLE
from core.exceptions import DatabaseError
from core.logging import logger


def get_example(model: EXAMPLE, db: Session, example: str) -> EXAMPLE | None:
    """Fetches the detail for a given example."""
    try:
        statement = (
            select(model)
            .where(model.example == example)
            .order_by(model.date_created.desc())
        )
        details = db.execute(statement).scalars().first()
        return details
    except Exception as e:
        std_out = f"Error fetching details for {example} from database."
        logger.error(std_out, exc_info=True)
        raise DatabaseError(std_out) from e


def create_example(model: EXAMPLE, db: Session, example_dict: dict) -> EXAMPLE | None:
    """Creates a new example in the database."""
    try:
        detail_data = model(**example_dict)
        db.add(detail_data)
        db.commit()
        db.refresh(detail_data)  # Refresh to ensure the object is up-to-date
        return detail_data
    except Exception as e:
        std_out = f"Error creating details for {example_dict['example']} in database."
        logger.error(std_out, exc_info=True)
        db.rollback()
        raise DatabaseError(std_out) from e


def update_example(
    model: EXAMPLE,
    db: Session,
    id: int,
    example: str,
) -> EXAMPLE | None:
    """Updates an existing example in the database."""
    try:
        statement = select(model).where(model.id == id)
        details = db.execute(statement).scalar_one()
        details.example = example
        db.commit()
        return details
    except Exception as e:
        std_out = f"Error updating details for {id} with {example} in database."
        logger.error(std_out, exc_info=True)
        db.rollback()
        raise DatabaseError(std_out) from e
