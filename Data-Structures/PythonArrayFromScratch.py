# we can learn how arrays work by creating our own array class from scratch
# basic array terminologies
# arrays have an index starting at 0
# arrays have elements accessed by the index
# array does have a length

class Array:
    def __init__(self, length):
        # represents arrays_length
        self.array_length = length
        # represents arrays elements
        self.elements = []
    
    # get elements total length
    def get_ElementsLength(self):
        return self.array_length
    
    # append elements value into array
    def appendElement(self, elementValue):
        self.elements.append(elementValue)
        self.array_length += 1

    # get element by index
    def getElementByIndex(self, index):
        return self.elements[index]

    # removes element by it's index
    def removeElementByIndex(self, index):
        return self.elements.pop(index)

    # shows all elements in array
    def showAllElements(self):
        # need to check if the array of elements is empty
        length = self.array_length
        
        if length <= 0:
            return "No Elements in array"

        if length > 0:
            return self.elements
   
    # clears out array
    def clearArray(self):
        return self.elements.clear()

    # sort array
    def sortArray(self):
        return self.elements.sort()

    # removes index of first elment specified
    def removeElementByWellElement(self, elementElement):
        return self.elements.remove(elementElement)

if __name__ == "__main__":
    array1 = Array(0)
    for i in range(1,5):
        array1.appendElement(i)
    print(array1.showAllElements())
