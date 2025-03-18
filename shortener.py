from flask import Flask, request, jsonify
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import hashlib
from models import URL, Base


class URLStore:
    def __init__(self, base_url: str = "http://localhost:5000/", db_url: str = "sqlite:///urls.db") -> None:
        """Initialize the URLStore with a base URL"""
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self._base_url = base_url

    def _encode_url(self, long_url: str) -> str:
        BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        hash_bytes = hashlib.sha256(long_url.encode()).hexdigest()
        hash_int = int(hash_bytes, 16)
       
        short_id = ""
        while hash_int > 0:
            hash_int, remainder = divmod(hash_int, 62)
            short_id = BASE62[remainder] + short_id
        
        return short_id[:6]
        
    def add_url(self, long_url: str) -> str:
        """Check for existing short URL / Add a new URL and return its short ID"""
        try:
            short_id = self._encode_url(long_url)
            existing_short_url = self.get_url(short_id)
            if existing_short_url:
                return f"{self._base_url}{short_id}"
            url = URL(short_id=short_id, long_url=long_url)
            self.session.add(url)
            self.session.commit()
            return f"{self._base_url}{short_id}"
        except SQLAlchemyError as e:
            self.session.rollback()
            raise

    def get_url(self, short_id: str) -> Optional[str]:
        """Get original URL from short ID"""
        try:
            url = self.session.query(URL).filter_by(short_id=short_id).first()
            return url.long_url if url else None
        except SQLAlchemyError as e:
            self.session.rollback()
            raise

    def __del__(self):
        """Cleanup database session"""
        self.session.close()

url_store = URLStore()