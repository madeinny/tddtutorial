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
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a text box
        # When she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list
        # There is still a text box inviting her to add another item

if __name__ == '__main__':
    unittest.main()