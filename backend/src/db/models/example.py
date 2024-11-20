from datetime import datetime as dt
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class EXAMPLE(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date_created: Mapped[dt] = mapped_column(default=func.now())
    date_updated: Mapped[dt] = mapped_column(default=func.now(), onupdate=func.now())
    example: Mapped[str] = mapped_column(String, index=True)

    def __repr__(self):
        return f"<EXAMPLE(id={self.id}, example='{self.example}')>"
