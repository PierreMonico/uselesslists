from selenium import webdriver 
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
            self.fail('Finish the test!')

            #He is invited to add an item to the list 


            #He enters a string and hits save 


            # page is refreshed and shows the list with the added item 


            #again, the textbox invites to add stuff 


            #he does it again and hits save 


            # page refreshes, and he wants to know how to get back to the page later
            #he sees the URL 


            #he then visits that url and finds his list again 
                        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
    
    
            
            
