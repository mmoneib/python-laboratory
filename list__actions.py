#!/user/bin/python
#TODO Add comments.

def obfuscate_by_sequence(originalList, sequence):
  tmpOriginalList=originalList
  obfuscatedList=[]
  while len(obfuscatedList) < len(tmpOriginalList):
    for i in sequence:
      index=int(i)
      if (index > len(tmpOriginalList)-1):
        index=len(tmpOriginalList)-1
      if (index < 0 ):
        break
      obfuscatedList.append(tmpOriginalList[index])
      tmpOriginalList.pop(index)
  return obfuscatedList

def deObfuscate_by_sequence(obfuscatedList, sequence):
  originalList=[]
  obfuscatedIndicesList=[]
  for i in range(0,len(obfuscatedList)):
    obfuscatedIndicesList.append(i)
  originalIndicesList=[]
  while len(originalIndicesList) < len(obfuscatedIndicesList):
    for i in sequence:
      index=int(i)
      if (index > len(obfuscatedIndicesList)-1):
        index=len(obfuscatedIndicesList)-1
      if (index < 0 ):
        break
      originalIndicesList.append(obfuscatedIndicesList[index])
      obfuscatedIndicesList.pop(index)
  originalList=[""]*len(originalIndicesList) # Because using insert flips some letters.
  for i in range(0,len(originalIndicesList)):
    originalList[originalIndicesList[i]]=obfuscatedList[i]
  return originalList
