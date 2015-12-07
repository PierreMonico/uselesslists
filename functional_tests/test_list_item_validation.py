from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #frog goes to the home page and accidentally inputs an empy item
        #it hits enter 
        
        #the page refreshes and tells him that an item can't be blank
        
        #he tries again with text, and it now works
        
        #like a perv, it tries to submit a blank item again 
        
        #a similar warning comes after refresh 
        
        #again, he can correct by putting in some text 
        
        self.fail('write me bitch')
