"""
SampleServiceのテスト
"""
import testbase
from bbs.service.sampleservice import SampleService

def test_add():
    session = testbase.testsession()
    service = SampleService(session)
    newdata = service.add_new('de', 1)
    session.commit()
    assert newdata is not None
    assert newdata.key == 'abcde'

    data = service.search_by_key('de')
    assert data is not None
