import pygame
import math
import time

class Enemy:
	def __init__(self,inPositionX,inPositionY,inSize):
		self.positionX = inPositionX
		self.positionY = inPositionY
		self.size = inSize
		self.image = pygame.image.load('/Users/phrk/ownCloud/Coding/python/pyteriods/enemyOne.png')

	def getX(self):
		return self.positionX

	def getY(self):
		return self.positionY

	def getSize(self):
		return self.size

	def paint(self,display,color):
		#pygame.draw.rect(display, color, [self.positionX,self.positionY,self.size,self.size])
		display.blit(self.image,(self.positionX,self.positionY-10))

	def move(self):
		self.positionX = 4*math.sin(self.positionY*0.05)+self.positionX
		self.positionY = self.positionY + 2




class Player:
	def __init__(self,inSize):
		self.size = inSize
		self.t1 = 0
		self.health = 5
		self.image = pygame.image.load('/Users/phrk/ownCloud/Coding/python/pyteriods/gameShip.png')

	def setX(self, position):
		self.positionX = position

	def getX(self):
		return self.positionX

	def setY(self, position):
		self.positionY = position

	def getY(self):
		return self.positionY

	def setHealth(self, inHealth):
		self.health = inHealth

	def getHealth(self):
		return self.health

	def getSize(self):
		return self.size

	def shoot(self,inSize):
		t0 = time.clock()
		if t0 > self.t1:
			self.t1 = t0+0.1
			newProjectile = Projectile(self.positionX,self.positionY,inSize)
			return newProjectile
		else:
			return 0

	def paint(self,inPositionX,inPositionY,display,color):
		display.blit(self.image,(self.positionX,self.positionY-10))
		#pygame.draw.rect(display, color, [inPositionX+4,inPositionY-2,3,3])
		#pygame.draw.rect(display, color, [inPositionX,inPositionY,self.size,self.size])

class Projectile:

	def __init__(self,inPositionX,inPositionY,inSize):
		self.positionX = inPositionX+11/2-3/2
		self.positionY = inPositionY
		self.size = inSize;
	
	def move(self):
		self.positionY = self.positionY - 2

	def getX(self):
		return self.positionX

	def getY(self):
		return self.positionY

	def getSize(self):
		return self.size

	def paint(self,display):
		pygame.draw.rect(display, (255,0,0), [self.positionX,self.positionY-10,self.size,self.size])


class GameMechanic:
	
	def checkDisplayBoundaries(self,objectToCheck,boundary,direction):
		for n in objectToCheck:
			if direction == 1:
				if n.getY() < boundary:
					objectToCheck.remove(n)
							
			elif direction == 2:		
				if n.getY() > boundary:
					objectToCheck.remove(n)
					
	
	def checkCollision(self,targetOne,targetTwo):
		for enemy in targetTwo:
			if enemy.getY()+enemy.getSize() >= targetOne.getY() and targetOne.getY()+targetOne.getSize() >= enemy.getY():
				if enemy.getX() <= targetOne.getX()+targetOne.getSize() and targetOne.getX() <= enemy.getX()+enemy.getSize():
					targetTwo.remove(enemy)
					return True			

	def drawHealth(self,inPlayer,display):
		pygame.draw.rect(display, (200,200,200), [748,8,50,9])
		for i in range(inPlayer.getHealth()):
			pygame.draw.rect(display, (0,150,0), [750+i*10,10,5,5])		

	def drawScore(self,score,display):
		font = pygame.font.Font(None, 36)
		text = font.render(str(score), 1, (255, 255, 255))
		textpos = text.get_rect()
		textpos.centerx = display.get_rect().centerx
		display.blit(text, textpos)





