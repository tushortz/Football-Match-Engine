import random

class Player:
	def __init__(self, name, skill, position, fitness):
		self.name = name
		self.skill = skill
		self.position = position
		self.luck = random.randint(0, 100) * 0.01
		self.fitness = fitness
		
	def shoot(self, goal_keeper):
		if ((self.skill.attack + self.skill.speed + self.fitness) * self.luck) and 
			(goal_keeper.skill.save + goal_keeper.skill.speed + goal_keeper.fitness) * goal_keeper.luck):
				return 1
		else:
			return 0			
