from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        #frog goes to the home page and accidentally inputs an empy item
        #it hits enter 
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        #the page refreshes and tells him that an item can't be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        #he tries again with text, and it now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')
        
        
        #like a perv, it tries to submit a blank item again 
        self.get_item_input_box().send_keys('\n')
        
        #a similar warning comes after refresh 
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
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
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")
        
    def test_error_messages_are_cleared_on_input(self):
        #frog starts a new list in a way thats causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        #it starts typing in the input box to clear the error 
        self.get_item_input_box().send_keys('a')
        
        # she is pleased to see that the error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
