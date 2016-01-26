from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #frog goes to the home page and accidentally inputs an empy item
        #it hits enter 
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        #the page refreshes and tells him that an item can't be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #he tries again with text, and it now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        
        #like a perv, it tries to submit a blank item again 
        self.get_item_input_box().send_keys('\n')
        
        #a similar warning comes after refresh 
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        

        #again, he can correct by putting in some text 
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
        
    def test_cannot_add_duplicate_items(self):
        #frog goes to the home page and starts a new list 
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')
        
        #frog accidentlly tries to submit a duplicate item 
        self.get_item_input_box().send_keys('Buy wellies\n')

        #it sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")
