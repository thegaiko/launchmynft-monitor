import time
from req import getLastCollection
from hook import sendHook

lastCollection = getLastCollection()
lastCollectionId = lastCollection['id']

sendHook(lastCollection)

while True:
    newCollection = getLastCollection()
    newCollectionId = newCollection['id']
    
    if newCollectionId != lastCollectionId:
        sendHook(newCollection)
        lastCollection = newCollection
        lastCollectionId = newCollectionId
    time.sleep(120)
