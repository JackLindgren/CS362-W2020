# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15, 2020

@author: Jack Lindgren
"""

from collections import defaultdict
import random

import Dominion

def get_player_names():
  """
  Returns a list of player names
  """
	return ["Annie", "*Ben", "*Carla"]

def get_box(num_victory):
  """
  Input: the number of victory cards
  Returns: a dictionary of cards
  The number of "Gardens" is determined by the # of victory cards
  """
  box = {}
  box["Woodcutter"] = [Dominion.Woodcutter()] * 10
  box["Smithy"] = [Dominion.Smithy()] * 10
  box["Laboratory"] = [Dominion.Laboratory()] * 10
  box["Village"] = [Dominion.Village()] * 10
  box["Festival"] = [Dominion.Festival()] * 10
  box["Market"] = [Dominion.Market()] * 10
  box["Chancellor"] = [Dominion.Chancellor()] * 10
  box["Workshop"] = [Dominion.Workshop()] * 10
  box["Moneylender"] = [Dominion.Moneylender()] * 10
  box["Chapel"] = [Dominion.Chapel()] * 10
  box["Cellar"] = [Dominion.Cellar()] * 10
  box["Remodel"] = [Dominion.Remodel()] * 10
  box["Adventurer"] = [Dominion.Adventurer()] * 10
  box["Feast"] = [Dominion.Feast()] * 10
  box["Mine"] = [Dominion.Mine()] * 10
  box["Library"] = [Dominion.Library()] * 10
  box["Gardens"] = [Dominion.Gardens()] * num_victory
  box["Moat"] = [Dominion.Moat()] * 10
  box["Council Room"] = [Dominion.Council_Room()] * 10
  box["Witch"] = [Dominion.Witch()] * 10
  box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
  box["Militia"] = [Dominion.Militia()] * 10
  box["Spy"] = [Dominion.Spy()] * 10
  box["Thief"] = [Dominion.Thief()] * 10
  box["Throne Room"] = [Dominion.Throne_Room()] * 10
  return box

def get_nv_nc(num_players):
  """
  Sets the number of Victory and Curse cards
  according to the number of players in the game
  """
  if num_players > 2:
      nV = 12
  else:
      nV = 8
  nC = -10 + 10 * num_players
  return nV, nC

def get_supply_order():
  """
  Returns a dictionary
  """
  supply_order  =  {
    0: ['Curse', 'Copper'],
    2: ['Estate', 'Cellar', 'Chapel', 'Moat'], 
    3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'], 
    4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 
      'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room'], 
    5: ['Duchy', 'Market', 'Council Room', 'Festival', 
      'Laboratory', 'Library', 'Mine', 'Witch'], 
    6: ['Gold', 'Adventurer'], 
    8: ['Province']
  }
  return supply_order

def get_supply_ten(box):
  """
  Input: box
    (a dict; keys are card names, values are arrays of cards)
  Returns:
  """
  boxlist = [k for k in box]
  random.shuffle(boxlist)
  random10 = boxlist[:10]
  supply = defaultdict(list,[(k,box[k]) for k in random10]) # CONFIRM WHAT THIS LINE DOES!
  return supply

def update_supply(supply, num_victory, num_curses, num_players):
  """
  Sets the supply of some of the items
  Modifies the given supply dict
  Nothing returned
  """
  supply["Copper"] = [Dominion.Copper()] * (60 - num_players * 7)
  supply["Silver"] = [Dominion.Silver()] * 40
  supply["Gold"] = [Dominion.Gold()] * 30
  supply["Estate"] = [Dominion.Estate()] * num_victory
  supply["Duchy"] = [Dominion.Duchy()] * num_victory
  supply["Province"] = [Dominion.Province()] * num_victory
  supply["Curse"] = [Dominion.Curse()] * num_curses

def get_players(player_names):
  """
  Takes the player_names list, creates the appropriate objects
  returns a list with the appropriate *Player objects
  """
  players = []
  for name in player_names:
    if name[0] == "*":
      players.append(Dominion.ComputerPlayer(name[1:]))
    elif name[0] == "^":
      players.append(Dominion.TablePlayer(name[1:]))
    else:
      players.append(Dominion.Player(name))
  return players

def shuffle_supply_order(supply_order):
  """
  Takes the supply order and randomly re-shuffles it
  """
  nums = list(supply_order.keys())

  random.shuffle(nums)

  new_supply_order = {}

  i = 0
  while i < len(nums):
    new_supply_order[i] = supply_order[nums[i]]
    i += 1

  return new_supply_order