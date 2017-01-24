import random

class Engine:
	def __init__(self, home_team, away_team):
		self.home_team = home_team
		self.away_team = away_team
		
	def scoreboard(self):
		print("%s %s : %s %s" % (self.home_team.name, self.home_team.score, self.away_team.score, self.away_team.name))
		
	def play(self, commetary=False):
		if commetary == True:
			print("%s vs %s\n" % (self.home_team, self.away_team))


		for x in range(self.home_team.chances):
			away_gk = self.away_team.players[0]
			away_def = random.choice(self.away_team.players[1:6])
			away_def_luck = random.random()
			home_player = random.choice(self.home_team.players[1:])

			# Opponent defends before player shoots
			if ((away_def.skill.defence * away_def_luck) < (home_player.skill.attack * home_player.luck)):

				if commetary == True:
					print("%s dribbles past %s" % (home_player.get_name(), away_def.get_name()))

				if home_player.shoot(away_gk) == 1:
					self.home_team.score += home_player.shoot(away_gk)

					if commetary == True:
						print("GOAL!!! Clinical finish from %s\n " % (home_player.get_name()))

				else:
					if commetary == True:
						print("MISS! Fine save from %s \n" % (away_gk.get_name()))


		for x in range(self.away_team.chances):
			home_gk = self.home_team.players[0]
			home_def = random.choice(self.home_team.players[1:6])
			home_def_luck = random.random()
			away_player = random.choice(self.away_team.players[1:])

			# Opponent defends before player shoots
			if ((home_def.skill.defence * home_def_luck) < (away_player.skill.attack * away_player.luck)):

				if commetary == True:
					print("%s dribbles past %s" % (away_player.get_name(), home_def.get_name()))

				if away_player.shoot(home_gk) == 1:
					self.away_team.score += away_player.shoot(home_gk)

					if commetary == True:
						print("GOAL!!! Clinical finish from %s \n" % (away_player.get_name()))

				else:
					if commetary == True:
						print("MISS! Fine save from %s \n" % (home_gk.get_name()))
		
	def winner(self):
		winner = None
		if self.home_team.score > self.away_team.score:
			winner = self.home_team
		elif self.home_team.score < self.away_team.score:
			winner = self.away_team
		
		return winner