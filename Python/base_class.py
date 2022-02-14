from typing import Any, Dict, List, Optional, Type, Union
from fastapi import HTTPException
from sqlalchemy import column, inspect
from sqlalchemy.orm.query import Query
from sqlalchemy.ext.declarative import as_declarative
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import logging
logger = logging.getLogger(__name__)

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# from typing import Any
# from sqlalchemy.ext.declarative import as_declarative, declared_attr
# @as_declarative()
# class Base:
#     id: Any
#     __name__: str
#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()

def get_primary_key(cls):
    inspect_model = inspect(cls)
    fields = [field.key for field in inspect_model.primary_key]
    if len(fields) > 1:
        raise Exception(f"Only one primary key is allowed; but {fields} found in {cls.__name__}")
    # endif
    try:
        name = fields[0]
        column = getattr(cls, name)
    except AttributeError as ae:
        logger.debug(ae)
        raise AttributeError(f"Given Base class {cls.__name__} does not have a primary key called {fields[0]}")
    return (column,name)

@as_declarative()
class Base:
    @classmethod
    def object_to_dict(
        cls,
        obj: Union[BaseModel, Dict[str, Any]],
    ):
        if isinstance(obj, BaseModel):
            obj = obj.dict(exclude_unset=True)
        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not a valid type to convert it as a dict; should be in type as BaseModel or dict")
        # endif
        return obj

    @classmethod
    def add_primary_key_criteria(cls, query: Query, obj: Union[BaseModel, dict, int]) -> Query:
        primary_key_column, column_name_str = get_primary_key(cls)
        value = None
        if isinstance(obj, BaseModel):
            obj = obj.dict(exclude_unset=True)
        elif isinstance(obj, int):
            value = obj

        if value == None:
            value = [value for key, value in obj.items() if key == column_name_str][0]

        return query.filter(primary_key_column == value)

    @classmethod
    def get_by(
        cls,
        db_session: Session,
        all_rows: Optional[bool] = False,
        return_type: Optional[Union[Union[BaseModel, dict], List[Union[BaseModel, dict]]]] = None,
        exception: Optional[Any] = None,
        **kwargs
    ):
        """
        Get Record(s) by given criteria

        **parameters**

        * `db_session` - SQLAlchemy session
        * `all_rows` - If True, return all rows, else return first row
        * `return_type` - The type of return object (pydantic, dict) [default=Sqlalchemy Query Result Object(s)].
        * `raise_exception` - If True, raise exception with `status_code = 400` if no record found.
        * `kwargs` - Keyword arguments to filter the query

        """
        instance = db_session.query(cls).filter_by(**kwargs)
        instance = instance.all() if all_rows else instance.first()
        if not instance and exception:
            raise exception
        if instance:
            instance = jsonable_encoder(instance)
        return return_type(**instance) if return_type else instance

    @classmethod
    def create(
            cls,
            db_session: Session,
            obj: Union[BaseModel, Dict[str, Any]],
            return_type: Optional[Union[BaseModel, dict]] = None,
            commit: Optional[bool] = True
    ):
        """
        Create a new record.

        **Parameters**
        * `db_session`: SQLAlchemy session
        * `obj`: A Pydantic model (schema) class or a dictionary
        * `return_type`: The type of return object (pydantic, dict) [default=Sqlalchemy Query Result Object].
        * `commit`: Commit the transaction [default=True].
        """
        # to get obj as dict

        obj = cls.object_to_dict(obj)

        new_obj = cls(**obj)  # type: ignore
        db_session.add(new_obj)
        if commit:
            db_session.commit()
            db_session.refresh(new_obj)

        if return_type:
            try:
                return return_type(**jsonable_encoder(new_obj))
            except Exception as pe:
                logger.debug(pe)
                raise HTTPException(status_code=500,
                    detail =f"{cls.__name__} Object has been saved.but, Error while returning it as {type(return_type)}.")
        else:
            return new_obj

    @classmethod
    def update(
            cls,
            db_session: Session,
            obj: Union[BaseModel, Dict[str, Any]],
            return_type: Type[BaseModel] = None,
            commit: Optional[bool] = True
    ):
        """
        Update an existing record.

        **Parameters**
        * `db_session`: SQLAlchemy session
        * `obj`: A Pydantic model (schema) class or a dictionary
        * `return_type`: The type of return object (pydantic, dict) [default=Sqlalchemy Query Result Object]
        * `commit`: Commit the transaction. [default=True]
        """
        # to get obj as dict
        obj = cls.object_to_dict(obj)

        query = db_session.query(cls)
        db_obj = cls.add_primary_key_criteria(query, obj).one_or_none()
        if not db_obj:
            primary_key_column, column_name_str = get_primary_key(cls)
            value = [value for key, value in obj.items() if key == column_name_str]
            raise HTTPException(
                status_code=404,
                detail=f"{cls.__name__} Object with {column_name_str} : {value} does not exist in the database"
            )
        # endif

        existing_data = jsonable_encoder(db_obj)
        update_data = obj

        for field in existing_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db_session.add(db_obj)
        if commit:
            db_session.commit()
            db_session.refresh(db_obj)
        # endif
        if return_type:
            try:
                return return_type(**jsonable_encoder(db_obj))
            except Exception as e:
                logger.debug(e)
                raise HTTPException(status_code=500,
                    detail =f"{cls.__name__} Object has been saved.but, Error while returning it as {type(return_type)}.")
        else:
            return db_obj

    @classmethod
    def delete(
            cls,
            db_session: Session,
            id: int,
            commit: Optional[bool] = True
    ):
        """
        Delete an existing record.

        **Parameters**
        * `db_session`: SQLAlchemy session
        * `id`: primary key's value of the record to be deleted
        * `commit`: Commit the transaction. [default=True]
        """
        query = db_session.query(cls)
        db_obj = cls.add_primary_key_criteria(query, id).one_or_none()
        primary_key_column, column_name_str = get_primary_key(cls)
        if not db_obj:
            raise HTTPException(
                status_code=404,
                detail=f"{cls.__name__} Object with {column_name_str}: {id} does not exist in the database")

        db_session.delete(db_obj)
        if commit:
            db_session.commit()

        return f"{cls.__name__} Object with {column_name_str}: {id} has been deleted."
