from typeclasses.objects import Object

class Document(Object):
    """
    Document class
    """
    
    def at_object_creation(self):
        super().at_object_creation()
        self.db.content = ""
    
    def read(self):
        self.msg(self.db.content)
    