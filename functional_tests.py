from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Dzonga has heard about a new To-Do List online app and go to 
		#check it out at its homepage
		self.browser.get('http://localhost:8000')

		#Notices the page title and header Mention To-Do lists 
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#User invited to enter a To-do Item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('plaeholder'),
				'Enter a to-do item'
		)

		#User types Read Capital in the 21st Centure in the text box (User
		# hobby is reading)
		inputbox.send_keys('Read Capital in the 21st Century')

		#When the user hits enter, the page update, and now lists 
		# "1. Read Capital in the 21st Century" as in item in a To-Do list 
		inputbox.send_keys(KEYS.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows.table.find_elements_by_tag_name('tr')
		self.assertTrue(
				any(row.text == '1:Capital in the 21st Century' for row in rows)
		)

		#There's still a textbox inviting the user to add another item 
		#User enters, "Drink more herbal tea"
		self.fail('Finish the test!')

		#The page updates, and now shows both items on the list 

		#User wonders whether site will remember the list. The user notices that 
		#the site has generated a unique url for him, 

		#User Visits URL and sees his To-Do list is still there 

		#Safisfied he goes to engage in passion 

if __name__ == '__main__':
	unittest.main(warnings='ignore')
