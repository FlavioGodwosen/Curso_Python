import unittest


class testCalculator(unittest.TestCase):
  #Setup
  def setUp(self):
      print("start")
  
  
  
  #test
  def test_sum(self):
      self.assertEqual(1+1, 2)
      
  #test
  def test_sum(self):
      self.assertEqual(2-1, 1)

  #Tear down
  
  def tearDown(self):
      print("End")
      
      
      if __name__== '__main__':
          unittest.main()