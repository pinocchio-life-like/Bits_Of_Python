class practice:
    def __init__(self, name):
        self._name = name
        
    def runner(self, name):
        print(f"{self.name}")
        
obj = practice("Eliyas")
obj.name = "Not you"
print(obj._name)