#!/usr/env/python
#TODO Move core of obfuscation to list__actions and leave here only conversion with lists.

def obfuscate_by_sequence(text, sequence):
  originalText=text
  obfuscatedText=""
  while len(obfuscatedText) < len(originalText):
    for i in sequence:
      index=int(i)
      if (index > len(text)-1):
        index=len(text)-1
      if (index < 0 ):
        break
      obfuscatedText+=text[index]
      text=text[0:index]+text[index+1:]
  print(obfuscatedText)

def deobfuscate_by_sequence(text, sequence):
  obfuscatedText=text
  originalText=""
  originalTextList=[]
  divisor=1
  count=0
  for i in range(0,len(obfuscatedText)):
    originalTextList.append(i)
  tmpOriginalList=originalTextList
  tmpObfuscatedList=[]
  while len(tmpObfuscatedList) < len(obfuscatedText):
    for i in sequence:
      index=int(i)
      if (index > len(tmpOriginalList)-1):
        index=len(tmpOriginalList)-1
      if (index < 0 ):
        break
      tmpObfuscatedList.append(tmpOriginalList[index])
      tmpOriginalList.pop(index)
  originalTextList=[""]*len(tmpObfuscatedList) # Because using insert flips some letters.
  for i in range(0,len(tmpObfuscatedList)):
    originalTextList[tmpObfuscatedList[i]]=obfuscatedText[i]
  print(originalTextList)

obfuscate_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234")
obfuscate_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1")
obfuscate_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "12")
obfuscate_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1358")
obfuscate_string("A cat is in the hat!", "1338")
#obfuscate_string(" t  cs  ant!iehtiahA", "1338")

deobfuscate_string("BDFHCGJLEKNPIORTMSVXQWZYUA", "1234")
#deobfuscate_string(" t  cs  ant!iehtiahA", "1338")
