class Engine:
	def __init__(self, home_team, away_team):
		self.home_team = home_team
		self.away_team = away_team
		
	def scoreboard(self):
		print("%s %s : %s %s" % (home_team.name, home_team.score, away_team.name, away_team.score)
		
	def action(self):
		pass
		# To print what happens in program
		
	def winner(self):
		winner = None
		if home_team.score > away_team.score:
			winner = home_team
		elif home_team.score < away_team.score:
			winner = away_team
		
		return winner
