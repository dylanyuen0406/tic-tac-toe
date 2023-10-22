import turtle

EAST, NORTH = 0, 90
LINE_LEN = 6
L1_X, L1_Y = -3, 1
L2_X, L2_Y = -3, -1
L3_X, L3_Y = -1, -3
L4_X, L4_Y = 1, -3


def main():
  global board, turn
  board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  setup()
  draw_lines()
  turn = 1
  screen.onclick(play)
  check_outcome(board)


def setup():
  global screen
  screen = turtle.Screen()
  screen.setup(800, 800)
  screen.title("TYM Python Beginner-Tic Tac Toe")
  screen.setworldcoordinates(-5, -5, 5, 5)
  turtle.speed("fastest")
  turtle.hideturtle()


def draw_lines():
  turtle.pencolor("black")
  turtle.pensize(10)
  turtle.penup()
  turtle.goto(L1_X, L1_Y)
  turtle.setheading(EAST)
  turtle.pendown()
  turtle.forward(LINE_LEN)
  turtle.penup()
  turtle.goto(L2_X, L2_Y)
  turtle.setheading(EAST)
  turtle.pendown()
  turtle.forward(LINE_LEN)
  turtle.penup()
  turtle.goto(L3_X, L3_Y)
  turtle.setheading(NORTH)
  turtle.pendown()
  turtle.forward(LINE_LEN)
  turtle.penup()
  turtle.goto(L4_X, L4_Y)
  turtle.setheading(NORTH)
  turtle.pendown()
  turtle.forward(LINE_LEN)


def draw(board):
  draw_lines()
  for row_index in range(3):
    for col_index in range(3):
      draw_move(row_index, col_index, board[row_index][col_index])


def draw_move(row_index, col_index, move):
  if move == 0:
    return
  intermediate_x = 2 * (col_index - 1)
  intermediate_y = 2 * (row_index - 1)
  if move == 1: draw_cross(intermediate_x, intermediate_y)
  else: draw_circle(intermediate_x, intermediate_y)


def draw_cross(x, y):
  turtle.color("blue")
  turtle.up()
  turtle.goto(x - 0.75, y - 0.75)
  turtle.down()
  turtle.goto(x + 0.75, y + 0.75)
  turtle.up()
  turtle.goto(x - 0.75, y + 0.75)
  turtle.down()
  turtle.goto(x + 0.75, y - 0.75)


def draw_circle(x, y):
  turtle.color("red")
  turtle.up()
  turtle.goto(x, y - 0.75)
  turtle.setheading(EAST)
  turtle.down()
  turtle.circle(0.75, steps=100)


def play(x, y):
  is_first_row = 1 < y and y < 3
  is_second_row = -1 < y and y < 1
  is_third_row = -3 < y and y < -1

  is_first_col = -3 < x and x < -1
  is_second_col = -1 < x and x < 1
  is_third_col = 1 < x and x < 3

  if is_first_row:
    row_index = 2
  elif is_second_row:
    row_index = 1
  elif is_third_row:
    row_index = 0
  else:
    return
  if is_first_col:
    col_index = 0
  elif is_second_col:
    col_index = 1
  elif is_third_col:
    col_index = 2
  else:
    return

  if board[row_index][col_index] != 0: return
  global turn
  if (turn == 1):
    board[row_index][col_index] = turn
    turn = 2
  else:
    board[row_index][col_index] = turn
    turn = 1
  draw(board)
  outcome=check_outcome(board)
  if outcome==1:
    screen.textinput("Game over!","X won!")
  if outcome==2:
    screen.textinput("Game over!","0 won!")
  if outcome==3:
    screen.textinput("Game over!","Tie!")
def check_outcome(board):
  if board[0][0]>0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
    return board[0][0]
  if board[1][0]>0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
    return board[1][0]
  if board[2][0]>0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
    return board[2][0]
  if board[0][0]>0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
    return board[0][0]
  if board[0][1]>0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
    return board[0][1]
  if board[0][2]>0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
    return board[0][2]
  if board[0][0]>0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    return board[0][0]
  if board[2][0]>0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
    return board[2][0]
  if check_tie(board):
    return 3
  else:
    return 0
def check_tie(board):
  num_pieces=0
  for row_index in range(3):
    for col_index in range(3):
      if(board[row_index][col_index]>0):
        num_pieces += 1
  if(num_pieces==9):
    return True
  return False


if __name__ == "__main__":
  main()