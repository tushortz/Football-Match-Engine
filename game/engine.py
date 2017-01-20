class Engine:
	def __init__(self, home_team, away_team):
		self.home_team = home_team
		self.away_team = away_team
		
	def scoreboard(self):
		self.home_team.score += self.home_team.players[0].shoot(self.away_team.players[0])
		self.away_team.score += self.away_team.players[0].shoot(self.home_team.players[0])

		print("%s %s : %s %s" % (self.home_team.name, self.home_team.score, self.away_team.name, self.away_team.score))
		
	def action(self):
		pass
		# To print what happens in program
		
	def winner(self):
		winner = None
		if self.home_team.score > self.away_team.score:
			winner = self.home_team
		elif self.home_team.score < self.away_team.score:
			winner = self.away_team
		
		return winner
