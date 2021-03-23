import boto3
from flask_caching import Cache
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy, Model

from config import Config


class CRUDMixin(Model):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        from app.services.utils import get_now
        self.deleted_at = get_now()
        return commit and db.session.commit()

    def delete_real(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


cors = CORS()
db = SQLAlchemy(model_class=CRUDMixin)
cache = Cache()
jwt = JWTManager()

s3 = boto3.client(
    "s3",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
)

sns = boto3.client(
    "sns",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_BUCKET_LOCATION
)

ses = boto3.client(
    "ses",
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1'
)
