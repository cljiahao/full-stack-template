from datetime import datetime as dt
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Example(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date_created: Mapped[dt] = mapped_column(default=func.now())
    date_updated: Mapped[dt] = mapped_column(default=func.now(), onupdate=func.now())
    example: Mapped[str] = mapped_column(unique=True, index=True)

    # Relationship to ParentExample
    parent_example: Mapped["ParentExample"] = relationship(
        "ParentExample", back_populates="examples"
    )
    # Foreign key to ParentExample
    parent_example_id: Mapped[int] = mapped_column(ForeignKey("parentexample.id"))

    def __repr__(self):
        return f"<Example(id={self.id}')>"
