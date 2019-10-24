#!/usr/bin/env python3
class Team(object):
    def win(self):
        print('Team is Winning the match')
    def buy(self):
        print('Team is buying players.')

class Dortmund(Team):
    def win(self):
        print('Dortmund is Winning the match')
    def buy(self):
        print('Dortmund is buying players.')

class Bayern(Team):
    def win(self):
        print('Bayern is Winning the match')
    def buy(self):
        print('Bayern is buying players.')
def run_twice(Team):
    Team.win()
    Team.win()

a = Team()
c = Bayern()
b = Dortmund()

print('a is Team?', isinstance(a, Team))
print('a is Bayern?', isinstance(a, Bayern))
print('a is Dortmund?', isinstance(a, Dortmund))

run_twice(c)