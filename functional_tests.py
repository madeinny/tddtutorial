import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        
        # Edith has heard about a cool new to-do app. She goes to check out
        # its homepage.
        self.browser.get('http://localhost:8000/')
        
        # She notices the page title and header metion to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys('\n')

        # When she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        # There is still a text box inviting her to add another item

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')