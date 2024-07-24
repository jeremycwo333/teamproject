from inventory.item import Item
class Camera(Item): 
   
    def __init__(self, assetTag, description, opticalZoom): 
        super().__init__(assetTag, description)
        self._opticalZoom = opticalZoom
        
        
    def getOpticalZoom(self): 
        return self._opticalZoom 
    
    def __str__(self):
        return super().__str__() +"{:<10}\n".format(self.getOpticalZoom())
                        