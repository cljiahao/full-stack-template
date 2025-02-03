import uuid
from datetime import datetime as dt
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class ParentExample(Base):
    id: Mapped[str] = mapped_column(
        primary_key=True, default=str(uuid.uuid4()), index=True
    )
    date_created: Mapped[dt] = mapped_column(default=func.now())
    date_updated: Mapped[dt] = mapped_column(default=func.now(), onupdate=func.now())

    # Relationship to Example
    examples: Mapped[list["Example"]] = relationship(
        "Example", back_populates="parent_example"
    )

    def __repr__(self):
        return f"<ParentExample(id={self.id}')>"
