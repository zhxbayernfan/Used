#!/usr/bin/env python3
Bundesliga = ['RBLeiβig','FCBayernMunich','BorussiaDortmund','Freiburg','Shalke04','M’Gladbach','BayerLeverkusen04','Wolfsburg']
Bundesliga.append('Frankfurt')
Bundesliga.append('Bremen')
Bundesliga.append('Augsburg')
Bundesliga.append('Dusseldorf')
Bundesliga.append('Hoffinheim')
Bundesliga.append('UnionBerlin')
Bundesliga.append('HerthaBerlin')
Bundesliga.append('Koln')
Bundesliga.append('Mainz')
Bundesliga.append('Paderborn')
def Bundesliga_ranking_all():
    i = 0
    file2 = open('E:/Python/013/write2.txt','w')
    file2.write('Bundesliga Team Ranks')
    file2.write('\n')
    file2.write('德甲联赛本赛季参赛队伍有%s支\n'%len(Bundesliga))
    file2.write('截至2019年9月23日中午12点\n')
    while i < len(Bundesliga):
        file2.write('排名第%s的队伍是%s\n'% (i+1,Bundesliga[i]))
        i = i + 1
    return
def Bundesliga_ranking_one():
    file3 = open('E:/Python/013/write3.txt','w')
    file3.write('你要查询的名次是第%s名\n'%j)
    if j - 1 < len(Bundesliga):
        file3.write('排名第%s的队伍是%s\n'%(j,Bundesliga[j-1]))
    if j - 1 >= len(Bundesliga):
        file3.write('Error')
    return
j = int (input('请输入你要查询的名次:'))
while j > 0:
    Bundesliga_ranking_one()
    break 
while j <= 0:
    print ('Error')
    break
file1 = open('E:/Python/013/write1.txt','w')
file1.write('Bundesliga Teams') 
file1.write('\n')
for team in Bundesliga:
    file1.write(team)
    file1.write('\n')
file1.close()
Bundesliga_ranking_all()