from game.engine import Engine
from player.player import Player
from player.skill import Skill
from team.team import Team

skill = Skill(80, 89, 20, 1, 66)
skill = Skill(90, 50, 40, 13, 55)

player = Player("Daniel", skill, 60, 100)
player2 = Player("Olu", skill, 70, 89)

players = []
players2 = []
players.append(player)
players2.append(player2)

home_team = Team("Chelsea", [4,3,3], players * 11)
away_team = Team("Arsenal", [4,4,2], players2 * 11)
engine = Engine(home_team, away_team)

for x in range(90):
	engine.scoreboard()