#!/usr/bin/emv python3
import argparse
import random
import math

def toss_coin():
  return randomly_choose(options=["H","T"])

def roll_dice():
  return randomly_choose(range(1,7))

def play_russian_roullette():
  return randomly_choose_with_bias(options=["CLICK", "BANG"], biases=[5, 1])

def navigate_randomly():
  return randomly_choose(options=["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
  
def move_randomly():
  return randomly_choose(options=["N", "S", "E", "W"])

def turn_randomly():
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
  return random.choice(options)

def random_sequence(targetAction="", delimiter="\n", sequenceSize=1):
  result=""
  for i in range(0, sequenceSize):
    result += eval(targetAction+"()")
    if i < sequenceSize - 1:
      result += delimiter
  return result

def histogram(targetAction="", sequenceSize=1):
  print

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
  
