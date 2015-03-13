# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import errno
import hashlib
import os

from django.conf import settings
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.utils.encoding import force_unicode

__all__ = ["HashedFileSystemStorage"]
__author__ = "pmeier82"


class ContentExists(Exception):
    pass


class HashedFileSystemStorage(FileSystemStorage):
    """`FileSystemStorage` subclass that manages file names by content hashes"""

    def get_available_name(self, name):
        raise ContentExists()

    def _get_content_name(self, name, content, chunk_size=None):
        dir_name = os.path.split(name)[0]
        file_name = self._generate_hash(content=content, chunk_size=chunk_size)
        return os.path.join(dir_name, file_name)

    def _generate_hash(self, content, chunk_size=None):
        if chunk_size is None:
            chunk_size = getattr(content, "DEFAULT_CHUNK_SIZE", File.DEFAULT_CHUNK_SIZE)
        hash_gen = hashlib.sha1()
        cursor = content.tell()
        content.seek(0)
        try:
            while True:
                data = content.read(chunk_size)
                if not data:
                    break
                hash_gen.update(data)
            return hash_gen.hexdigest()
        finally:
            content.seek(cursor)

    def save(self, name, content):
        if getattr(settings, "DEBUG", None) is True:
            print "{}::save({})".format(self.__class__.__name__, name)
        if name is None:
            name = content.name
        name = self._get_content_name(name, content)
        name = self._save(name, content)
        return force_unicode(name.replace('\\', '/'))

    def _save(self, name, content):
        new_name = self._get_content_name(name=name, content=content)
        try:
            return super(HashedFileSystemStorage, self)._save(new_name, content)
        except ContentExists:
            pass
        except OSError, e:
            if e.errno == errno.EEXIST:
                pass
            else:
                raise
        return new_name

    def delete(self, name):
        if getattr(settings, "DEBUG", None) is True:
            print "{}::delete({})".format(self.__class__.__name__, name)
        return super(HashedFileSystemStorage, self).delete(name)


if __name__ == "__main__":
    pass
