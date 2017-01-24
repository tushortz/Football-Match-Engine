import random

class Player:
	def __init__(self, name, position, skill):
		self.name = name
		self.position = position
		self.skill = skill
		self.luck = random.randint(0, 100) * 0.01
		self.fitness = 100

		if position.upper() not in ("GK", "DF", "MF", "FW"):
			raise(InvalidPlayerPositionError(self, "--> %s" % position, "Options are: GK, DF, MF, FW"))

	def __str__(self):
		return "%s %s (%s)" % (self.position, self.name, self.skill)

	def __repr__(self):
		return "%s %s (%s)" % (self.position, self.name, self.skill)

	def get_name(self):
		return self.name

	def shoot(self, goal_keeper):
		if ((self.skill.attack + self.skill.speed + self.fitness)*self.luck > 
			(goal_keeper.skill.save + goal_keeper.skill.speed + goal_keeper.fitness)*goal_keeper.luck):
			self.fitness -= random.randint(0,20)

			return 1
		return 0			


class InvalidPlayerPositionError(Exception):
	def __init__(self, name, position, message):
		self.name = name
		self.position = position
		self.message = message