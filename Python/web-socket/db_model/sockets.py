from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from fastapi import WebSocket
import pickle

from core.base_class import Base

class Active_Sockets(Base):
    __tablename__ = "active_sockets"
    user_name = Column(String, unique=True, primary_key=True)
    _socket_byte_str= Column(bytes, unique=True)

    @property
    def web_socket(self) -> WebSocket:
        return pickle.loads(self._socket_byte_str)