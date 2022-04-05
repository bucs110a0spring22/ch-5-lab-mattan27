'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

def drawSquare(darty=None, width=0, top_left_x=0, top_left_y=0):
  darty.up()
  darty.goto(top_left_x, top_left_y)
  for i in range (4):
    darty.down()
    darty.forward(width)
    darty.right(90)
    darty.up()

def drawLine(darty=None, x_start=0, y_start=0, x_end=0, y_end=0):
  darty.up()
  darty.goto(x_start, y_start)
  darty.down()
  darty.goto(x_end, y_end)
  darty.up

def drawCircle(darty=None, radius=0):
  darty.circle(radius, steps=360)

def setUpDartboard(myscreen=None, darty=None):
  myscreen.setworldcoordinates(-2, -2, 2, 2)
  drawSquare(darty, 2, -1, 1)
  drawLine(darty, -1, 0, 1, 0)
  drawLine(darty, 0, 1, 0, -1)
  drawCircle(darty, 1)

def isInCircle(darty=None, circle_center_x=0, circle_center_y=0, radius=0):
  if darty.distance(0,0) < radius:
    return 'Is In Circle'
    darty.dot(10, 'green')
  else:
    return 'Is Not In Circle'
    darty.dot(10, 'red')

def throwDart(darty=None, in_color='green', out_color='red'):
  x = random.random()
  negx = random.uniform(-1,1)
  resultx = x * negx
  y = random.random()
  negy = random.uniform(-1,1)
  resulty = y * negy
  darty.up()
  darty.goto(resultx, resulty)
  if darty.distance(0,0) >= 1:
    darty.color(out_color)
  else:
    darty.color(in_color)
  darty.dot()
  darty.color('black')
  darty.down()

def playDarts(darty=None):
  Ascore = 0
  Bscore = 0
  for i in range (10):
    throwDart(darty, 'yellow')
    if isInCircle(darty=darty, radius=1):
      Ascore += 1
      print("Player A hit")
    throwDart(darty, in_color='purple')
    if isInCircle(darty=darty, radius=1):
      Bscore += 1
      print("Player B hit")
    if Ascore > Bscore:
      print("Winner: Player A!")
    elif Ascore == Bscore:
      print("Winner: Tie!")
    else:
      print("Winner: Player B!")

def montePi(darty=None, num_darts=0):
  inside_count=0
  outside_count=0
  for i in range(0, num_darts):
    throwDart(darty=darty)
    if isInCircle(darty=darty, circle_center_x=0, circle_center_y=0, radius=1):
      inside_count = outside_count +1
  return((inside_count/num_darts)*4)

def draw_shape(myscreen, shape):

  myscreen.setworldcoordinates(-500, -500, 500, 500)
  
  if shape == "square":
    for i in range(0,4):
      turtle.fd(50)
      turtle.lt(90)
    turtle.fd(75)
  if shape == "triangle":
    for i in range(0,3):
      turtle.fd(50)
      turtle.lt(120)
    turtle.fd(75)
  if shape == "hexagon":
    for i in range(0,6):
      turtle.fd(50)
      turtle.lt(60)
    turtle.fd(75)

turtle.goto(-250,0)

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
  # Get number of darts for simulation from user
  # Note continuation character <\> so we don't go over 78 columns:
  print("This is a program that simulates throwing darts at a dartboard\n" \
    "in order to approximate pi: The ratio of darts in a unit circle\n"\
    "to the total number of darts in a 2X2 square should be\n"\
    "approximately  equal to pi/4")
  print("=========== Part A ===========")

  #Create window, turtle, set up window as dartboard
  window = turtle.Screen()
  darty = turtle.Turtle()
  darty.speed(0) # as fast as it will go!
  setUpDartboard(window, darty)

  # Loop for 10 darts to test your code
  for i in range(10):
    throwDart(darty)
  print("\tPart A Complete...")
  print("=========== Part B ===========")
  darty.clear()
  setUpDartboard(window, darty)
  playDarts(darty)
  print("\tPart B Complete...")
  # Keep the window up until dismissed
  print("=========== Part C ===========")
  darty.clear()
  setUpDartboard(window, darty)
    
  # Includes the following code in order to update animation periodically
  # instead of for each throw (saves LOTS of time):
  BATCH_OF_DARTS = 5000
  window.tracer(BATCH_OF_DARTS)

  # Conduct simulation and print result
  number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
  approx_pi = montePi(darty, number_darts)
  print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
  print("\tPart C Complete...")

  draw_shape("square")
  draw_shape("triangle")
  draw_shape("hexagon")
  
  # Don't hide or mess with window while it's 'working'
  window.exitonclick()
  
main()
