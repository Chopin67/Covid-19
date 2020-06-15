import turtle

bob = turtle.Turtle()
bob.speed('slow')
bob.circle(100)
bob.color('blue')
bob.forward(100)
bob.left(90) #going up right side of square
bob.color('orange')
bob.forward(200)
bob.left(90) #going across top side of square
bob.color('blue')
bob.forward(200)
bob.left(90)      #going across left side of square
bob.color('orange')
bob.forward(200)
bob.left(90)      #finishing square
bob.color('blue')
bob.forward(100)
bob.forward(50)    #starting rotunda
bob.left(90)
bob.forward(100)   #right side of square
bob.left(90)
bob.forward(100)   #top side of square
bob.left(90)
bob.forward(85)   #left side of square
bob.left(90)
bob.forward(20)  #bottom side of square
bob.left(90)
bob.forward(85)  #first column
bob.right(90)
bob.forward(20)
bob.right(90)
bob.forward(85) #second column
bob.left(90)
bob.forward(20)
bob.left(90)
bob.forward(85) #third column
bob.right(90)
bob.forward(20)
bob.right(90)
bob.forward(85) #fourth column
bob.left(90)
bob.forward(20)
bob.left(90)
bob.forward(85)


bob.done()

