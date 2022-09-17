from pprint import pprint
import time
from req import getLastCollection
from hook import sendHook

lastCollection = getLastCollection()
lastCollectionId = [lastCollection['id']]

sendHook(lastCollection)

while True:
    newCollection = getLastCollection()
    newCollectionId = newCollection['id']
    
    if newCollectionId not in lastCollectionId:
        sendHook(newCollection)
        lastCollection = newCollection
        lastCollectionId.append(newCollectionId)
    time.sleep(30)
