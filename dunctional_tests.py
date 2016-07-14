#coding=utf-8 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.broswer.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.broswer.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        table = self.broswer.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')

        self.assertTrue(
            any(rows.text == '1: Buy peacock feathers' for row in rows)
        )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warning='ingnore')


# bowser = webdriver.Firefox()
# bowser.get('http://localhost:8000')
# assert 'Django' in bowser.title
# bowser.quit()