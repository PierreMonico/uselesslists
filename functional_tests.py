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

            #Frog visits hte website to add some items he wants to remember 
            self.browser.get('http://localhost:8000')

            #He sees the website title and the header of the to do list 
            self.assertIn('To-Do', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            #He is invited to add an item to the list 
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )

            #He enters 'Buy peacock feathers' and hits save 
            inputbox.send_keys('Buy peacock feathers')

            # page is refreshed and shows the list with '1: Buy peacock feathers' 
            inputbox.send_keys(Keys.ENTER)
            
            table = self.browser.get_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows)
            )
            

            #again, the textbox invites to add stuff 
            self.fail('finish the test!!')

            #he does it again and hits save 


            # page refreshes, and he wants to know how to get back to the page later
            #he sees the URL 


            #he then visits that url and finds his list again 
                        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    
            
            
