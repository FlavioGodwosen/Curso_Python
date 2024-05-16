import pytest

@pytest.fixture(scope="session")
def setup():
    print("begin")
    yield
    print("End")
    
#test
def test_sum(setup):
  assert 1+1 == 2
      
#test
def test_sum(setup):
  assert 2-1 == 1    
  
#test
def test_sum(setup):
  assert 1+5 == 6
      
#test
def test_sum(setup):
  assert 2-4 == -2     