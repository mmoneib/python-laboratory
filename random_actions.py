#!/usr/bin/env python3
"""
Random Actions

A collection of functions used to provide convenicence and consolidation of random decisions.
"""
import argparse
import random
import math

#TODO Add possibility to use parameters for triggering a sequence of actions.
#TODO Add an action to generate truth tables.

def toss_coin():
  """
  Simulates a fair coin toss.
   
  Returns:
    A string in the form of "H" for head or "T" for  tail.
  """
  return randomly_choose(options=["H","T"])

def left_or_right:
  """
  Picks left or right direction randomly.

  Returns:
    A string in the form of "L" for left or "R" for right.
  """
  return randomly_choose(options=["L","R"])

def up_or_down:
  """
  Picks up or down movement randomly.

  Returns:
    A string in the form of "U" for up and "D" for down.
  """
  return randomly_choose(options=["U","D"])

def roll_dice():
  """
  Simulates a roll of a dice.

  Returns:
    An integer from 1 to 6.
  """
  return randomly_choose(range(1,7))

def play_russian_roullette():
  """
  Simulates a Russian Roullete game using a pistol with a capacity of 6 bullets and is only loaded with 1.

  Returns:
    The string "CLICK" 1/6 of the times signifying a miss, or the string "BANG" 5/6 of the tumes signifying a hit. 
  """
  return randomly_choose_with_bias(options=["CLICK", "BANG"], biases=[5, 1])

def navigate_randomly():
  """
  Simulates a random navigator which gives back one of the eight main directions from a compass.

  Returns:
    The string "N" for north, "NE" for north ease, "E" for east, "SE" for south east, "S" for south, "SW" for south west, "W" for west, or "NW" for morth west. 
  """
  return randomly_choose(options=["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
  
def move_randomly():
  """
  Simulates a random navigator which gives back one of the four main directions from a compass.

  Returns:
    The string "N" for north, "E" for east, "S" for south, or "W" for west. 
  """
  return randomly_choose(options=["N", "S", "E", "W"])

def turn_randomly():
  """
  Simulates a random planar movement or rotation with respect to the object itself rather than the main directions of a compass.

  Returns:
    The string "F" for forward, "B" for backward, "L" for leftward, or "R" for rightward. 
  """
  return randomly_choose(options=["F", "B", "L", "R"])

def randomly_choose_with_bias(options=[], biases=[]):
  biasedOptions=[]
  for divisor in range(2, max(biases)+1): # TODO: Move LCF of list.
    tmpSum = 0
    for weight in biases:
      tmpSum = tmpSum + (int(weight) % int(divisor))
    if tmpSum == 0:
      break
    divisor = divisor + 1
  if divisor > max(biases):
    divisor = 1
  biases[:] = [int(w/divisor) for w in biases] # The : inside [] is to change the same list. The division must be int.
  for i in range(0, len(biases)):
    biasedOptions = biasedOptions + [options[i]] * biases[i]
  return random.choice(biasedOptions)

def randomly_choose(options=[]):
  """
  A simple random choice out of the members of the supplied list.

  Args:
    options (dictionary): The list of options from which a random choice will be done.

  Returns:
    An object as chosen from the list. 

  """
  return random.choice(options)

def random_sequence_of_actions(targetAction="", delimiter="\n", sequenceSize=1):
  """
  Calls another action a specified number of times to get a random sequence of outputs seperated by the specified delimiter.

  Args:
    targetAction (str): The name of the action (function) within this script to be called and for which the sequence of output is expected.
    delimiter (str): The delimiter to be used to separate betwee the output of each iteration. Defaults to a new line.
    sequenceSize (int): The number of iterations through which the action will be called.

  Returns:
    A string containin the sequence of outputs from the action separated by the delimiter.
  """
  result=""
  for i in range(0, sequenceSize):
    result += eval(targetAction+"()")
    if i < sequenceSize - 1:
      result += delimiter
  return result

def histogram(targetAction="", sequenceSize=1):
  print("Not implemented.")


if __name__ == "__main__":
  functionsList = [func for func in dir() if callable(eval(func)) and not func.startswith("__")]
  parser = argparse.ArgumentParser(description="Random generation set of actions.")
  parser.add_argument("--action", "-a", action="store", choices=functionsList, required=True)
  parser.add_argument("--biases", "-b", action="store")
  parser.add_argument("--options", "-o", action="store")
  parser.add_argument("--sequence-size", "-s", action="store")
  parser.add_argument("--target-action", "-t", action="store", choices=functionsList)
  args = parser.parse_args()
  if args.options and args.biases:
    assert len(options) == len(biases)
  callArgs=""
  if args.options:
    options=args.options.split(",")
    callArgs = callArgs + "options={},".format(options)
  if args.biases:
    biases = list(map(int,args.biases.split(",")))
    callArgs = callArgs + "biases={},".format(biases)
  if args.sequence_size:
    sequenceSize = int(args.sequence_size)
    callArgs = callArgs + "sequenceSize={},".format(sequenceSize)
  if args.target_action:
    callArgs = callArgs + "targetAction=\"{}\",".format(args.target_action)
  print(eval(args.action+"({})".format(callArgs), globals(), locals()))
  
