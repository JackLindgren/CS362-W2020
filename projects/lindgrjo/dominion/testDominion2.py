# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15, 2020

@author: Jack Lindgren
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = testUtility.get_player_names()

#number of curses and victory cards
nV, nC = testUtility.get_nv_nc(len(player_names))

#Define box
box = testUtility.get_box(nV)

supply_order = testUtility.get_supply_order()

# shuffle the supply order 
# so that it doesn't correspond with the actual prices
supply_order = testUtility.shuffle_supply_order(supply_order)

#Pick 10 cards from box to be in the supply.
supply = testUtility.get_supply_ten(box)

#The supply always has these cards
testUtility.update_supply(supply, nV, nC, len(player_names))

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.get_players(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)