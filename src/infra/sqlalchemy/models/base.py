from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from core import settings
from utils.converters import to_snake_case


class Base(DeclarativeBase):
    metadata_obj = MetaData(naming_convention=settings.postgres.name_convention)

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return to_snake_case(cls.__name__) + "s"

    id: Mapped[int] = mapped_column(primary_key=True)
