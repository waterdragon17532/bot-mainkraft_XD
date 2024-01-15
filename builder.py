import mcpi.minecraft as minecraft
import mcpi.entity as entity
import collections
from random import* 
collections.Iterable = collections.abc.Iterable

from time import sleep

#mc = minecraft.Minecraft.create("localhost", 4711)
mc = minecraft.Minecraft.create('83.147.245.230', 4711)
mc.postToChat('6')
#print(entity.SLIME)

#mc.spawnEntity(*mc.player.getPos(),entity.SLIME.id)

'''
while True:
    chatEvent = mc.events.pollChatPosts()
    print(chatEvent)
    sleep(10)
'''

# Установка блока земли
#mc.setBlock(*mc.player.getPos(), 2)
 #mc.setBlock(*mc.player.getPos(), 113)

#крепость
def bastion ():
    startx,starty,startz = mc.player.getPos()
    wherex = startx + 20
    #пол
    h = 14
    w1,w2 = 30,30
    for x in range(w1):
        for z in range(w2):
            if x == 0 or x == w1-1 or z == 0 or z == w2-1:
                for y in range (h+randint(-1,1)): 
                    mc.setBlock(wherex + x,starty + y,startz + z,112 )
            else :
                mc.setBlock(wherex + x,starty,startz + z,112 )
bastion()
