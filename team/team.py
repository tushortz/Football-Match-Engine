class Team:
	def __init__(self, name, formation, players):
		self.name = name
		self.formation = formation
		self.players = players
		self.result = None
		self.score = 0
		
	def result(self, opponent):
		
		if opponent.score > self.score:
			self.result = "loss"
		elif opponent.score < self.score:
			self.result = "win"
		else:
			self.score = "draw"
		
