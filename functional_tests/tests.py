from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

class NewVisitorTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):

        #Frog visits the website to add some items he wants to remember 
        self.browser.get(self.live_server_url)

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

        #He enters 'Buy peacock feathers' 
        inputbox.send_keys('Buy peacock feathers')
        
        # when she hits enter she is taken to a new URL,
        # and now the page lists "1: buy peacock feathers" as a to-do item
        inputbox.send_keys(Keys.ENTER)
        
        frog_list_url = self.browser.current_url
        self.assertRegex(frog_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        

        #again, the textbox invites to add stuff 
        inputbox = self.browser.find_element_by_id('id_new_item')

        #he does it again and hits save 
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # page refreshes, and shows both items in the list 
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # a new user, cat, comes along to the site
        
        ## we use a new browser to make sure nothing from frogs info is left  
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #cat visits the site; there is no sign of frogs list 
        self.browser.get(self.live_server_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #cat starts a new list by entering a new item 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        #cat gets his own unique url 
        cat_list_url = self.browser.current_url
        self.assertRegex(cat_list_url, '/lists/.+')
        self.assertNotEqual(cat_list_url, frog_list_url)
        
        #again, there is no trace of frogs list 
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
            
    def test_layout_and_styling(self):
        #Frog goes to the home page 
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        #he notices the inputbox is nicely centered 
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5 
        )
        
        #he starts a new list and sees the input is nicely centered there too 
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5 
        )        
