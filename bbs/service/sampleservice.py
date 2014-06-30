"""
sampleテーブルを管理するクラス
"""
import datetime

from ..models import Sample
class SampleService(object):
    def __init__(self, session):
        self._session = session
        self._basestring = 'abc'
    def add_new(self, key, status=1):
        keystring = self._basestring + key
        now       = datetime.datetime.now()
        data = Sample(key=keystring, timestamp=now, status=status)
        self._session.add(data)
        return data
    def search_by_key(self, key):
        for row in self._session.query(Sample).filter_by(key=key):
            return row
