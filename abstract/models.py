from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import uuid


class AbstractManager(models.Manager):
    def get_object_by_public_id(self,public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance

        except (ObjectDoesNotExist,ValueError, TypeError):
            return Http404



class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True,unique=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)

    objects = AbstractManager()

    class Meta:
        abstract = True

