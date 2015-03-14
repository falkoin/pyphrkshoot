import pygame
import gameModule
import random

pygame.init()

colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorRed   = (255,0,0)
colorGrey  = (100,100,100)
gameWidth  = 800
gameHeight = 600
gameMargin = 20
playerSize = 11;
startX     = gameWidth/2-5;
startY     = gameHeight-50;

gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption('Pysteriods')

gameClock = pygame.time.Clock()
gameRunning = True

myGameMechanic = gameModule.GameMechanic();
myPlayer = gameModule.Player(playerSize);
myPlayer.setX(startX);
myPlayer.setY(startY);

missle = []
enemy  = [];
xChange = 4;
enemySpawn = 5000;
gameTime = 0;
score = 0;

while gameRunning:
	gameTime = gameTime + gameClock.get_time()
	pygame.event.pump()
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		gameRunning = False
	if pygame.key.get_pressed()[pygame.K_RIGHT]:
		newPosition = myPlayer.getX()+xChange
		if newPosition+myPlayer.getSize() > gameWidth:
			newPosition = gameWidth - myPlayer.getSize()
		myPlayer.setX(newPosition)
	elif pygame.key.get_pressed()[pygame.K_LEFT]:	
		newPosition = myPlayer.getX()-xChange
		if newPosition < 0:
			newPosition = 0
		myPlayer.setX(newPosition)
	if pygame.key.get_pressed()[pygame.K_SPACE]:
		newMissile = myPlayer.shoot(3)
		if newMissile != 0:
			missle.append(newMissile)

	if pygame.event.get(pygame.QUIT):
		gameRunning = False	

	gameDisplay.fill(colorBlack)

	if gameTime > enemySpawn:
		enemyPositionX = random.randint(gameMargin, gameWidth-gameMargin)
		enemySpawn = enemySpawn+1000
		enemy.append(gameModule.Enemy(enemyPositionX,10,25)) 

	myPlayer.paint(myPlayer.getX(),myPlayer.getY(),gameDisplay,colorWhite)

	myGameMechanic.checkDisplayBoundaries(missle,0,1) #removes missle when outside of display
	myGameMechanic.checkDisplayBoundaries(enemy,gameHeight,2) #removes enemy when outside of display

	for n in missle:
		n.paint(gameDisplay)
		n.move()
	for n in enemy:
		n.paint(gameDisplay,colorGrey)
		n.move()
	for n in missle:
		if myGameMechanic.checkCollision(n,enemy) == True:
			missle.remove(n)
			score = score+1

	if myGameMechanic.checkCollision(myPlayer,enemy) == True:
		myPlayer.setHealth(myPlayer.getHealth()-1)
		if myPlayer.getHealth() < 1:
			print('NOOBIE')

	myGameMechanic.drawHealth(myPlayer,gameDisplay)
	myGameMechanic.drawScore(score,gameDisplay)
	pygame.display.update()
	gameClock.tick(60)	
pygame.quit()
quit()

# get_fps()