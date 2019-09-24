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
file1 = open('E:/Python/014/write1.txt','w')
file1.write('Bundesliga Teams') 
file1.write('\n')
for team in Bundesliga:
    file1.write(team)
    file1.write('\n')
file1.close()
def Bundesliga_ranking_one():
    file2.write('你要查询的名次是第%s名\n'%j)
    file2.write('排名第%s的队伍是%s\n'%(j,Bundesliga[j-1]))
    return
j = int (input('请输入你要查询的名次:'))
file2 = open('E:/Python/014/write2.txt','w')
while j > 0 & j - 1 < len(Bundesliga):
    if j < 5:
        file2.write('欧冠区\n')
        Bundesliga_ranking_one()
    elif j < 8:
        file2.write('欧联区\n')
        Bundesliga_ranking_one()
    elif j < 16:
        file2.write('非保级区\n')
        Bundesliga_ranking_one()
    else:
        file2.write('保级区\n')
        Bundesliga_ranking_one()
    break
while j - 1 >= len(Bundesliga):
    file2.write('Error\n')
while j <= 0:
    file2.write('Error\n')
    break