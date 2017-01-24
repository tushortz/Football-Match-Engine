class Team:
	def __init__(self, name, players):
		self.name = name
		self.players = players
		self.result = None
		self.score = 0
		self.chances = 0

		df, mf, fw = 0,0,0
		for player in players:
			if player.position.upper() == "DF":
				df += 1
			elif player.position.upper() == "MF":
				mf += 1
			elif player.position.upper() == "FW":
				fw += 1

			self.chances += player.skill.passing

		self.chances = (self.chances) % len(players)
		self.formation = [df, mf, fw]
		
		if sum(self.formation) != 10:
			raise(InvalidFormationError(self, self.formation, "You should have 10 players in the team aside from the GK"))

		if (1 >= len(players) > 11):
			raise(InvalidNumberOfPlayerError(players), "Invalid number of players: Must be 11 players")

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name		

	def result(self, opponent):
		
		if opponent.score > self.score:
			self.result = "loss"
		elif opponent.score < self.score:
			self.result = "win"
		else:
			self.result = "draw"
		
		return self.result


class InvalidFormationError(BaseException):
	def __init__(self, team, formation, message):
		self.team = team
		self.formation = formation 
		self.message = message


class InvalidNumberOfPlayerError(BaseException):
	def __init__(self, team_number):
		self.team_number = team_number
