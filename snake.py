# Snakes Game
# Use Arrow Keys to play, SpaceBar for pausing/Resuming and ESC Key for exiting

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr()
win=curses.newwin(20,80,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key=KEY_RIGHT				#Initializing values
score=0

snake=[[4,10], [4,9], [4,8]]  			#Initial snake co-ordinates
food=[10,20]							#Initial food co-ordinates

win.addch(food[0], food[1], '*')		#Prints the food

while key!=27:							#while ESC is not pressed
	win.border(0)
	win.addstr(0,2, 'Score:' +str(score) + ' ')      	#printing score
	win.addstr(0, 27, 'Snake')						    #printing snake string
	win.timeout(150-(len(snake)/5+len(snake)/10)%120)	#increase the speed of snake as its length increase

	prevkey=key 										#previous key pressed
	event=win.getch()
	key=key if event==-1 else event

	if key==ord(' '): 									#if spacebar is pressed, wait for another
		key=-1											#one (pause/resume)
		while key!=ord(' '):
			key=win.getch()
		key=prevkey
		continue

	if key not in[KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,27]:		#if an invalid key pressed
		key=prevkey


	'''calculate the new co-ordinates of the head of the snake.
		Note: len(snake) increases.
		This is taken care of later at [1].
	'''

	snake.insert(0, [snake[0][0]+(key==KEY_DOWN and 1)+(key==KEY_UP and -1), snake[0][1]+(key==KEY_LEFT and -1)+(key==KEY_RIGHT and 1)])

	#if snake crosses the boundries, make it enter from other side.

	if snake[0][0]==0:
		snake[0][0]=18
	if snake[0][1]==0:
		snake[0][1]=58
	if snake[0][0]==19:
		snake[0][0]=1
	if snake[0][1]==59:
		snake[0][1]=1

	'''
		Exit if snake crosses the boundries (Uncomment to enable)

		if snake[0][0]==0 or snake[0][0]==19 or snake[0][1]==0 or snake[0][1]==59: break

		if snakes over run itself
	'''
	if snake[0] in snake[1:]: break

	if snake[0]==food:												#when snake eat the food
		food=[]
		score+=1
		while food==[]:
			food=[randint(1,18), randint(1,58)]						#calculating next food co-ordinates
			if food in snake:
				food=[]
		win.addch(food[0], food[1], '*')
	else:
		last=snake.pop()											#[1] if it doesnot eat the food, length decreases
		win.addch(last[0],last[1], ' ')
	win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()

print '\nscore : ' +str(score)
print 'Thanks for playing...'