#!/usr/bin/env python3
import csv

headers = ['Number','Name','Year_of_Birth','Nationality','Position','Last_Team_before_Bayern',"With_'_Now"]

rows = [
        ['01','Manuel Neuer','1988','Deutsch','Goal Keeper','Shalke04',''],
        ['04','Nikolas Sule','1995','Deutsch','Center Back','Hoffinheim',''],
        ['05','Benjamin Pavard','1996','France','Center Back','Stuttgart',''],
        ["05'",'Mats Hummels','1988','Deutsch','Center Back','Dortmund','Dortmund'],
        ['06','Thiago Alcantara','1991','Spain','Center MidFielder','Barcelona',''],
        ["07'",'Franck Ribery','1983','France','Left MidFielder','Olympique de Marseille','Florence'],
        ['08','Javi Martinez','1988','Spain','Defence MidFielder','Athletic Club Bilbao',''],
        ['09','Robert Lewandowski','1988','Poland','Center Forward','Dortmund',''],
        ["09'",'Mario Manzukic','1986','Croatia','Center Forward','Wolfsburg','Juventus'],
        ['10','Philippe Coutinho','1992','Brazil','Attack MidFielder','Barcelona',''],
        ["10'",'Arjen Robben','1984','Netherland','Right MidFielder','Real Madrid','Retired'],
        ['11','Mickael Cuisance','1999','France','Center MidFielder',"M'Gladbach",''],
        ["11'",'James Rodriguez','1991','Columbia','Attack MidFielder','Real Madrid','Real Madrid'],
        ['12','Berni','2005','Deutsch','Mascot','/',''],
        ["13'",'Rafinha','1985','Brazil','Right Back','Genoa','Flamingo'],
        ['14','Ivan Perisic','1989','Croatia','Left MidFielder','Internazionale Milano',''],
        ["14'",'Juan Bernat','1993','Spain','Left Back','Valencia','Paris Saint German'],
        ['14"','Xabi Alonso','1981','Spain','Defence MidFielder','Real Madrid','Retired'],
        ['15','Jann Fiete Arp','2000','Deutsch','Second Striker','Hamburg',''],
        ['17','Jerome Boateng','1988','Deutsch','Center Back','Manchester City',''],
        ['18','Leon Goretzka','1995','Deutsch','Attack MidFielder','Shalke04',''],
        ["18'",'Miroslav Klose','1978','Deutsch','Center Forward','Bremen','Retired as Coach'],
        ['19','Alphonso Davies','2000','Canada','Left MidFielder','Vancouver Whitecaps FC',''],
        ["19'",'Mario Gotze','1992','Deutsch','Second Striker','Dortmund','Dortmund'],
        ['21','Lucas Hernandes','1996','France','Center Back','Atheletico Madrid',''],
        ["21'",'Philipp Lahm','1983','Deutsch','Right Back','Bayern Youth Team','Retired'],
        ['22','Serge Gnabry','1995','Deutsch','Right Wing Forward','Hoffinheim',''],
        ['24','Corentine Tolisso','1994','France','Center MidFielder','Olympique Lyonnais',''],
        ['25','Thomas Muller','1989','Deutsch','Second Striker','Bayern Youth Team',''],
        ['26','Sven Ulreich','1988','Deutsch','Goal Keeper','Stuttgart',''],
        ['27','David Alaba','1992','Austria','Left Back','Bayern Youth Team',''],
        ["28'",'Holger Badstuber','1989','Deutsch','Center Back','Bayern Youth Team','?'],
        ['29','Kingsley Coman','1996','France','Left Wing Forward','Juventus',''],
        ["31'",'Bastian Schweinsteiger','1984','Deutsch','Center MidFielder','Bayern Youth Team','Chicago'],
        ['32','Joshua Kimmich','1995','Deutsch','Right Back','Stuttgart',''],
        ['33','Lucas Mai','2000','Deutsch','Center Back','Bayern Youth Team',''],
        ["33'",'Mario Gomez','1985','Deutsch','Center Forward','Stuttgart','Stuttgart'],
        ['36','Christian Fruchtl','2000','Deutsch','Goal Keeper','Bayern Youth Team',''],
        ['39','Ron Thorben Hoffmann','1999','Deutsch','Goal Keeper','Bayern Youth Team','']
    ]

with open('E:/python/017/FCBayern_Players.csv','w',newline='')as file1:
    file1_csv = csv.writer(file1)
    file1_csv.writerow(headers)
    file1_csv.writerows(rows)
