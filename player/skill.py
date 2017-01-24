class Skill:
	def __init__(self, save, defence, passing, midfield, attack, speed):
		self.save = save
		self.defence = defence
		self.passing = passing
		self.midfield = midfield
		self.attack = attack
		self.speed = speed

	def __str__(self):
		return "GK:%s, DEF:%s, PASS:%s, MID:%s, ATT:%s, SPD:%s" % (
			self.save, self.defence, self.passing, self.midfield, self.attack, self.speed)

	def __repr__(self):
		return "GK:%s, DEF:%s, PASS:%s, MID:%s, ATT:%s, SPD:%s" % (
			self.save, self.defence, self.passing, self.midfield, self.attack, self.speed)