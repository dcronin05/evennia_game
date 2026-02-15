from typeclasses.objects import Object

class Document(Object):
    """
    Document class
    """
    
    def at_object_creation(self):
        super().at_object_creation()
        self.db.content = ""
    
    def read(self, caller):
        self.caller.msg(self.db.content)
    