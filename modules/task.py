"""
Write a class in which its one method accepts a string from console and 
another method to print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

"""

class EvenString:

    def __init__(self):
        self.text = ""
        self.output = ""
    
  
    
    def enter_text(self):
        self.text = input('Enter the string...')

        for i in self.text:
            if (self.text.index(i) % 2 == 0):
                self.output +=i 

        return self.output
    

    
    def print_output(self):
        print("The resulted string is:", self.output)

if __name__ == "__main__":
    es = EvenString()
    es.enter_text()
    es.print_output()

       

   
    
   
    

    
    