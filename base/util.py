# -*- coding: utf-8 -*-

from django.db.models import FileField
from django.core.files.storage import default_storage
from model_utils import Choices

__all__ = ["file_cleanup"]
__author__ = "pmeier82"

AccessChoices = Choices("private", "public")

if __name__ == "__main__":
    pass
