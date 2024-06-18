from decimal import Decimal
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, func, MetaData, inspect
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    convention = {
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    }

    metadata = MetaData(naming_convention=convention)

    def to_dict(self, nested=True):
        data = {}
        mapper = inspect(self)
        for column in mapper.attrs:
            value = getattr(self, column.key)
            if nested and hasattr(value, 'to_dict'):
                data[column.key] = value.to_dict(nested=False)
            elif nested and isinstance(value, list):
                data[column.key] = [item.to_dict(nested=False) for item in value]
            else:
                data[column.key] = self._parse_value(value)

        return data

    def _parse_value(self, value):
        if isinstance(value, Decimal):
            return float(value)
        elif isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, uuid.UUID):
            return str(value)
        return value
