from orm_base import Base
from sqlalchemy import Column, Integer, UniqueConstraint, Identity
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Department(Base):
    """a division of a large organization of university dealing with a specific subject, commodity,
    or area of activity."""
    __tablename__ = "departments"  # Give SQLAlchemy th name of the table.
    name: Mapped[str] = mapped_column('name', String(50), nullable=False, primary_key=True)
    abbreviation: Mapped[str] = mapped_column('abbreviation', String(6), nullable=False)
    chairName: Mapped[str] = mapped_column('chair_name', String(80), nullable=False)
    building: Mapped[str] = mapped_column('building', String(10), nullable=False)
    office: Mapped[int] = mapped_column('office', Integer, nullable=False)
    description: Mapped[str] = mapped_column('description', String(80), nullable=False)
    # __table_args__ can best be viewed as directives that we ask SQLAlchemy to
    # send to the database.  In this case, that we want two separate uniqueness
    # constraints (candidate keys).
    __table_args__ = (UniqueConstraint("abbreviation"),
                        UniqueConstraint("chair_name"),
                        UniqueConstraint("building", "office"),
                        UniqueConstraint("description"))

    def __init__(self, abbreviation: str, chair_name: str, building: str, office: int, description: str):
        self.abbreviation = abbreviation
        self.chairName = chair_name
        self.building = building
        self.office = office
        self.description = description

    def __str__(self):
        return f"Department: {self.abbreviation}, Chair: {self.chair_name}" \
               f"\nBuilding: {self.building}, Office: {self.office}\nDescription: {self.description}"
