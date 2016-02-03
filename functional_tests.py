from selenium import webdriver 
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
		self.fail('Finish the test!')

		#User invited to enter a To-do Item right away

		#User types Read Capital in the 21st Centure in the text box (User
		# hobby is reading)

		#When the user hits enter, the page update, and now lists 
		# "1. Read Capital in the 21st Century" as in item in a To-Do list 

		#There's still a textbox inviting the user to add another item 
		#User enters, "Drink more herbal tea"

		#The page updates, and now shows both items on the list 

		#User wonders whether site will remember the list. The user notices that 
		#the site has generated a unique url for him, 

		#User Visits URL and sees his To-Do list is still there 

		#Safisfied he goes to engage in passion 

if __name__ == '__main__':
	unittest.main(warnings='ignore')
