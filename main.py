import turtle
# from practice import *

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
turtle.tracer(0)


RAD = 20  # radius of circle
PAD = 10  # space between edges of circles

board = []
turn = "red"


# build board
for h in range(6):
  row = []
  for j in range(7):
    row.append("")
  board.append(row)



# for r in board:
#   print(r)






def draw_circle(x, y, color):
  t.color(color)
  t.penup()
  t.goto(x, y - RAD)
  t.pendown()
  t.begin_fill()
  t.circle(20)
  t.end_fill()


def draw_board():
  t.color("blue")
  t.penup()

  # draw rectangle
  t.goto(-160 - 40, 120 + 40)
  t.pendown()
  t.begin_fill()
  for i in range(2):
    t.forward(40 + 50*6 + 40)
    t.right(90)
    t.forward(40 + 50*5 + 40)  
    t.right(90)
  t.end_fill()
  
  # draw circles
  t.color("white")
  for row in range(6):
    for col in range(7):
      draw_circle(-160 + col * 50, 120 - row * 50, "white")

  # labels cols
  t.penup()
  t.goto(-160, -200)
  t.color("blue")

  for i in range(7):
    t.goto(-160+i*50, -200)
    t.write(i+1, align="center", font=("Arial", 15, "normal"))
  
  

def drop(col):
  for row in range(5, -1, -1):
    if board[row][col] == "":  
      board[row][col] = turn
      draw_circle(-160+col*50, 120 - 50*row, turn)
      return True

  
  print("Column is full, try again")
  return False


def line_win(start_row, start_col, step_row, step_col):
  streak = 0  # streak of the same color back to back
  streak_chip = None
  curr_row = start_row
  curr_col = start_col

  # while curr_row is in range and curr_col is in range
  while (0 <= curr_row <= 5) and (0 <= curr_col <= 6):
    if board[curr_row][curr_col] == streak_chip != "":  # continuing streak
      streak = streak + 1
    else:  # restart the count
      streak = 1
      streak_chip = board[curr_row][curr_col]

    if streak == 4:
      print(streak_chip, "Won!")
      return True

    curr_row = curr_row + step_row
    curr_col = curr_col + step_col

  return False


def horz_win():
  for i in range(6):
    if line_win(i, 0, 0, 1):
      return True
  return False
  

def vert_win():
  for i in range(6):
    if line_win(0, i, 1, 0):
      return True
  return False


def diag_win():
  start_row = 5
  start_col_ltr = 3
  start_col_rtl = 3

  for i in range(6):
    if (line_win(start_row, start_col_ltr, -1, 1) or
       line_win(start_row, start_col_rtl, -1, -1)):
      return True

    if start_col_ltr>0:
      start_col_ltr = start_col_ltr - 1
      start_col_rtl = start_col_rtl + 1
      
    elif start_col_ltr == 0:
      start_row = start_row - 1

  



draw_board()


while True:
  ''' use input to ask the player to choose a column.
      if the column is between 1 and 7 (including both)
      then use the drop function to drop in that column
  '''
  playerinput = int(input(turn + ", drop your chip into a column -> "))

  # add an else and print "invalid input, try again"
  if playerinput >= 1 and playerinput <= 7 and drop(playerinput-1):
    ''' switch turns '''
    if turn == "red":
      turn = "yellow"
    elif turn == "yellow":
      turn = "red" 
    
  else:
    print("invalid input, try again")


  if horz_win() or vert_win() or diag_win():
    break
  










''' FUNCTIONS
  - return is a command that ends the execution of a function
    on the line that it is used. the code will then jump back
    to where the function was called.
  - often there is a value associated with the return. this value
    gets sent back to where the function was called.
  - for example, the len() function returns a number:

      if len("Harry") > 3:
        print("yes")


'''





screen.mainloop()
