
## Import
import math

## Class definition and list of methods
class ConvexPolygon:
    
    ## Class constructor
    def __init__(self, v):
        self.v = v
        
    ## Gets the list of vertices that the object holds
    def getVertices(self):
        return self.v
    
    ## Changes one vertex in the list with another
    def setVertex(self, i, x, y):
        v[i] = [x,y]
        
    ## Gets the length between two specified vertices
    def getLength(self, i, j):
        return math.sqrt( (self.v[i][0] - self.v[j][0])**2 + (self.v[i][1] - self.v[j][1])**2 )
    
    ## Gets the interior angle of a specified vertex
    def getInteriorAngle(self, i):
        
        ## Notes: "firstLength", "secondLength", etc are denoted as the different lengths required to solve the function 
        ## given above in the requirements. These lengths are separated by addition or subtraction or multiplication in
        ## the equation above
        
        ## If the "i" given is the first or last element in the list of vertices, than doing i+1 for the last element would
        ## cause an error, likewise for i-1 for the first element. To fix this issue, three different situations are set up
        ## (i = first, i = last, i = any other place) in order to find the correct lengths without casuing an error. The
        ## different scenarios play around with the fact that the next vertex for the last vertex in the list is actually 
        ## the first one
        
        ## Gets the lengths if i is the last element in the list
        if (i+1) == len(self.v):
            
            firstLength = (math.sqrt( (self.v[i][0] - self.v[0][0])**2 + (self.v[i][1] - self.v[0][1])**2 ))**2
            secondLength = (math.sqrt( (self.v[i-1][0] - self.v[i][0])**2 + (self.v[i-1][1] - self.v[i][1])**2 ))**2
            thirdLength = (math.sqrt( (self.v[i-1][0] - self.v[0][0])**2 + (self.v[i-1][1] - self.v[0][1])**2 ))**2
            fourthLength = (math.sqrt( (self.v[i][0] - self.v[0][0])**2 + (self.v[i][1] - self.v[0][1])**2 ))*2
            fifthLength = math.sqrt( (self.v[i-1][0] - self.v[i][0])**2 + (self.v[i-1][1] - self.v[i][1])**2 ) 
               
        ## Gets the lengths if i is the first element in the list
        elif i == 0:
            
            firstLength = (math.sqrt( (self.v[i][0] - self.v[i+1][0])**2 + (self.v[i][1] - self.v[i+1][1])**2 ))**2
            secondLength = (math.sqrt( (self.v[len(self.v)-1][0] - self.v[i][0])**2 + (self.v[len(self.v)-1][1] - self.v[i][1])**2 ))**2
            thirdLength = (math.sqrt( (self.v[len(self.v)-1][0] - self.v[i+1][0])**2 + (self.v[len(self.v)-1][1] - self.v[i+1][1])**2 ))**2
            fourthLength = (math.sqrt( (self.v[i][0] - self.v[i+1][0])**2 + (self.v[i][1] - self.v[i+1][1])**2 ))*2
            fifthLength = math.sqrt( (self.v[len(self.v)-1][0] - self.v[i][0])**2 + (self.v[len(self.v)-1][1] - self.v[i][1])**2 )
        
        ## Gets the lengths if i is any other elment place in the list
        else:
            
            firstLength = (math.sqrt( (self.v[i][0] - self.v[i+1][0])**2 + (self.v[i][1] - self.v[i+1][1])**2 ))**2
            secondLength = (math.sqrt( (self.v[i-1][0] - self.v[i][0])**2 + (self.v[i-1][1] - self.v[i][1])**2 ))**2
            thirdLength = (math.sqrt( (self.v[i-1][0] - self.v[i+1][0])**2 + (self.v[i-1][1] - self.v[i+1][1])**2 ))**2
            fourthLength = (math.sqrt( (self.v[i][0] - self.v[i+1][0])**2 + (self.v[i][1] - self.v[i+1][1])**2 ))*2
            fifthLength = math.sqrt( (self.v[i-1][0] - self.v[i][0])**2 + (self.v[i-1][1] - self.v[i][1])**2 )
        
        ## Final calculation to find the interior angle and then returns it
        interiorAngle = math.acos((firstLength + secondLength - thirdLength)/(fourthLength*fifthLength))
        return interiorAngle
    
## Function to see if all edges and interior angles in the polyon are equal
def isRegularPolygon(p):
    
    ## Gets the base measurements of the polyon
    baseAngle = p.getInteriorAngle(0)
    baseLength = p.getLength(0,1)
    
    ## Loops through every angle and edge and compares them to the base measurement, retuning False if any
    ## measurement does not equal the base measurement and returning True if all of them equal the base measurement
    for i in range(len(p.getVertices())-1):
        
        if baseAngle == p.getInteriorAngle(i+1):
            
            if baseLength == p.getLength(i,i+1):
                ## Makes the conditional block work
                1
            
            else:
                return False
            
        else:
            return False
        
    return True



## Data Entry
v = [[0.75,3.5],[2.5,2.75],[2.25,-0.5],[-0.75,-1.5],[-0.25,2.25]]
test_polygon = ConvexPolygon(v)
test_polygon_2 = ConvexPolygon([[-1.25,-0.75],[-1.25,1.25],[0.75,1.25],[0.75,-0.75]])

## Possible Test Casea and Answers

#test_polygon.getVertices() == [[0.75,3.5],[2.0,3.0],[2.25,-0.5],[-0.75,-1.5],[-0.25,2.25]]
#test_polygon.getLength(2,3) == 3.1622776601683795
#test_polygon.getInteriorAngle(3) == 1.1164942401015803
#isRegularPolygon(test_polygon) == False
#isRegularPolygon(test_polygon_2) == True
