class Parent():
    def __init__(self, lastname, eyecolor):
        print("PArent Constructor Called")
        self.lastname=lastname
        self.eyecolor=eyecolor
    def show_info(self):
        print ("lastname- "+self.lastname)
        print ("Eye Color-"+self.eyecolor)
        
class Child(Parent):
    def __init__(self, lastname, eyecolor,numberoftoys):
        print("Child Constructor Called")
        Parent.__init__(self, lastname, eyecolor)
        self.numberoftoys = numberoftoys

    def show_info(self):
        print ("last name- "+ self.lastname)
        print ("Eye Color- "+ self.eyecolor)
        print ("Number of Toys# "+ str(self.numberoftoys))
        
billy_cyrus = Parent ("cyrus", "Blue")
#billy_cyrus.show_info()
#print(billy_cyrus.lastname)
miley_cyrus=Child("Cyrus", "Ocean Green", 7)
#print (miley_cyrus.lastname)
#print (miley_cyrus.numberoftoys)
miley_cyrus.show_info()
