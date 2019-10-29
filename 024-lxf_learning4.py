#!/usr/bin/env python3

class Team(object):
    __slots__ = ('name', 'rank') 

class FinishingTeam(Team):
    pass

s = Team() 
s.name = 'Bayern' 
s.rank = 1 
# ERROR: AttributeError: 'Team' object has no attribute 'score'
try:
    s.score = 95
except AttributeError as e:
    print('AttributeError:', e)

g = FinishingTeam()
g.score = 95
print('g.score =', g.score)