from game.engine import Engine
from player.player import Player
from player.skill import Skill
from team.team import Team
from random import randint as _

#------------------------------------
# def _(a=0, b=100):
# 	return random.randint(a, b)

# save, defence, passing, midfield, attack, speed
# skillgk1 = Skill(_(60, 100), _(),  _(), _(), _(), _(50))
# skillgk2 = Skill(_(60, 100), _(),  _(), _(), _(), _(50))

# skilldef1 = Skill(_(0,10), _(50),  _(20), _(), _(), _(50))
# skilldef2 = Skill(_(0,10), _(50),  _(20), _(), _(), _(50))

# skillmid1 = Skill(_(0,10), _(30), _(50), _(50), _(50), _(50))
# skillmid2 = Skill(_(0,10), _(30),  _(50), _(50), _(50), _(50))

# skillatt1 = Skill(_(0,5), _(10),  _(50), _(40), _(50), _(50))
# skillatt2 = Skill(_(0,5), _(10),  _(50), _(40), _(50), _(50))


# players1 = []
# players1.append(Player(1, skillgk1, "GK"))
# for _ in range(4):
# 	players1.append(Player(_+2, skilldef1, "DF"))
# for _ in range(3):	
# 	players1.append(Player(_+2, skillmid1, "MF"))
# for _ in range(3):	
# 	players1.append(Player(_+2, skillatt1, "FW"))


# players2 = []
# players2.append(Player(1, skillgk2, "GK"))
# for _ in range(4):
# 	players2.append(Player(_+2, skilldef1, "DF"))
# for _ in range(4):	
# 	players2.append(Player(_+2, skillmid1, "MF"))
# for _ in range(2):	
# 	players2.append(Player(_+2, skillatt1, "FW"))

# for x in players1:
# 	print(x) 
# print(players2)
#--------------------------------------

# Generate random data
# Skill(save, defence, passing, midfield, attack, speed)
# Player(name, position, skill)
players1 = [
	Player("Courtois", "GK", Skill(_(60,100), _(0,100),  _(0,100), _(0,100), _(0,100), _(50,100))),

	Player("Azpilicueta", "DF", Skill(_(0,10), _(60,100),  _(20,100), _(0,100), _(0,100), _(50,100))),
	Player("Luiz", "DF", Skill(_(0,10), _(50,100),  _(60,100), _(0,100), _(50,100), _(50,100))),
	Player("Cahill", "DF", Skill(_(0,10), _(50,100),  _(20,100), _(0,100), _(0,100), _(50,100))),

	Player("Moses", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(50,100), _(50,100))),
	Player("Matic", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(50,100), _(50,100))),
	Player("Kante", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(50,100), _(50,100))),
	Player("Alonso", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(50,100), _(50,100))),

	Player("Hazard", "FW", Skill(_(0,5), _(10,100),  _(50,100), _(40,100), _(70,100), _(60,100))),
	Player("Costa", "FW", Skill(_(0,5), _(10,100),  _(50,100), _(40,100), _(70,100), _(60,100))),
	Player("Pedro", "FW", Skill(_(0,5), _(10,100),  _(50,100), _(40,100), _(70,100), _(60,100)))
]

players2 = [
	Player("Cech", "GK", Skill(_(60,100), _(0,100),  _(0,100), _(0,100), _(0,100), _(50,100))),

	Player("Paulista", "DF", Skill(_(0,10), _(50,100),  _(20,100), _(0,100), _(0,100), _(50,100))),
	Player("Mustafi", "DF", Skill(_(0,10), _(50,100),  _(20,100), _(0,100), _(0,100), _(50,100))),
	Player("Koscielny", "DF", Skill(_(0,10), _(50,100),  _(20,100), _(0,100), _(0,100), _(50,100))),
	Player("Monreal", "DF", Skill(_(0,10), _(50,100),  _(20,100), _(0,100), _(0,100), _(50,100))),

	Player("Ramsey", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(70,100), _(50,100))),
	Player("Xhaka", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(60,100), _(50,100))),
	Player("Sanchez", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(70,100), _(50,100))),
	Player("Oezil", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(75,100), _(50,100))),
	Player("Iwobi", "MF", Skill(_(0,10), _(30,100), _(50,100), _(50,100), _(50,100), _(50,100))),

	Player("Giroud", "FW", Skill(_(0,5), _(10,100),  _(50,100), _(40,100), _(70,100), _(60,100)))
]

home_team = Team("Chelsea", players1)
away_team = Team("Arsenal", players2)
engine = Engine(home_team, away_team)

engine.play(True)
engine.scoreboard()