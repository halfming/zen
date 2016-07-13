#coding=utf-8 
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.broswer = webdriver.Firefox()
        self.broswer.implicitly_wait(3)  #等待

    def tearDown(self):
        self.broswer.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.broswer.get('http://localhost:8000')

        self.assertIn('To-Do',self.broswer.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warning='ingnore')


# bowser = webdriver.Firefox()
# bowser.get('http://localhost:8000')
# assert 'Django' in bowser.title
# bowser.quit()