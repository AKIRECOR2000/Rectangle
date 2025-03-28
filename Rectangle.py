#Akire Cormier, CIS261, Rectangle
from dataclasses import dataclass

@dataclass
class Rectangle:
    height: int
    width: int
    
    def getPerimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter

    def getArea(self):
        area = self.height * self.width
        return area

    def getStr(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "* "
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w 
        return s
    
def main():
     print("The Rectangle Calculator")
     print()
    
     again = "yes"
     while again.lower() == "yes":
         height = int(input("Height: "))
         width = int(input("Width: "))
        
         rectangle = Rectangle(height, width)
         print("Perimeter:", rectangle.getPerimeter())
         print("Area: ", rectangle.getArea())
         print(rectangle.getStr())
        
         again = input("Continue? yes/no: ".lower())
         print()
        
     print("See ya!")
    
if __name__ == "__main__":
        main()
                  
