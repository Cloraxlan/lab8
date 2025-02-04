from models import AttractionModel

class AttractionService:
   def __init__(self):
       self.model = AttractionModel()

   def create(self, params):
       return self.model.create(params)

   def update(self, item_id, params):
       return self.model.update(item_id, params)

   def delete(self, item_id):
       return self.model.delete(item_id)

   def list(self):
       response = self.model.list_items()
       return response
  
   def get_by_id(self, item_id):
       response = self.model.get_by_id(item_id)
       return response
   
   def visit(self, item_id):
       return self.model.visit(item_id)
   
   def state_search(self, state):
       return self.model.list_items(f"AND State = '{state}'")
       
