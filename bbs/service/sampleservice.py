"""
sampleテーブルを管理するクラス
"""
import datetime

from ..models import Sample
class SampleService(object):
    u"""
    sampleテーブル管理クラス

    Attrubutes:
      _session: DBセッション
      _basestring: キー用のプレフィックス
    """
    def __init__(self, session):
        self._session = session
        self._basestring = 'abc'
    def add_new(self, key, status=1):
        u"""
        新レコード追加

        Arguments:
          key(str): レコードのユニークキー
          status(int): レコードステータス
        """
        keystring = self._basestring + key
        now       = datetime.datetime.now()
        data = Sample(key=keystring, timestamp=now, status=status)
        self._session.add(data)
        return data
    def search_by_key(self, key):
        u"""
        keyで検索

        Arguments:
          key(str): 検索キー。プレフィックスは付けないこと
        """
        keystring = self._basestring + key
        for row in self._session.query(Sample).filter_by(key=keystring):
            return row
