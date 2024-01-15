from javascript import require, On, Once, AsyncTask, once, off
from time import sleep

mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

RANGE_GOAL = 0
BOT_USERNAME = '666'

#bot = mineflayer.createBot({ 'host': '26.6.17.205', 'port': 25565, 'username': '666', 'hideErrors': False })


bot = mineflayer.createBot({ 'host': '83.147.245.230', 'port': 25565, 'username': '666', 'hideErrors': False,'checkTimeoutInterval': 60 * 1000000 })

bot.loadPlugin(pathfinder.pathfinder)

def check_almaz_aroud():
    #i - id блока
    i = 56
    return bot.findBlocks({'point':bot.entity.position, 'matching':i,'maxDistance':500})

def blockface(playerName):
    if playerName == BOT_USERNAME:
        return bot.blockAt(bot.entity.position.offset(0, 0, 0))#в какую сторону смотри бот +-
        #можно сделать чтобы бот вставал на алмазики
        # функции с инвентарем 
    else:
        return bot.blockAt(bot.players[playerName].entity.position.offset(0, -1, 0))

def dig_down():
    #try:
    while bot.canDigBlock(blockunder()):
        print("я копаю")
        bot.dig(blockunder())

    bot.chat("Can't dig deeper")
    #except Exception:
        #bot.chat("Stopped digging")
        
def blockunder():
    block = bot.blockAt(bot.entity.position.offset(0, -1, 0))
    return block
def kakoi_uygolb():
    i = 0
    for item in bot.inventory.items():
        if item.name == 'diamond':
            return i
        i += 1
        
@On(bot, 'spawn')
def handle(*args):
    print("666 spawned 👋")   
    @On(bot, 'chat')
    def handleMsg(this, sender, message, *args):
        movements = pathfinder.Movements(bot)
        print("Получил сообщение", sender, message)
        if sender and (sender != BOT_USERNAME):
            bot.chat('Ты сказал: ' + message)
            if 'ко мне' in message:
                player = bot.players[sender]
                print("Цель:", player)
                target = player.entity
                if not target:
                    bot.chat("Не вижу цель!")
                    return

                pos = target.position
                bot.pathfinder.setMovements(movements)
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, RANGE_GOAL))
            if 'алмазики ищи' in message:
                cors = check_almaz_aroud()
                # print (cors.__dict__)
            
                if len(list(cors))>0:    
                    block = cors[0]
                    bot.chat(f"{block.x} {block.y} {block.z}")
                    bot.pathfinder.setGoal(pathfinder.goals.GoalNear(block.x, block.y, block.z, RANGE_GOAL))
                    
                    #bot.dig(block.x,block.y,block.z,lambda result: print('Копание завершено') if result else print('Не удалось начать копание'))
                    
                else :
                    bot.chat("капец нету")
            if 'алмазики выкидовай' in message:
                inventory = bot.inventory
                index = kakoi_uygolb()
                #print(index)
                #print(inventory.items()[index])
                bot.tossStack(inventory.items()[index], 1)

once(bot, 'login')

#bot.setControlState('sprint', True)


#target = bot.blockAt(bot.entity.position.offset(0, -1, 0))
#print(target)
#print(bot.entity.position.offset(0, -1, 0))

def say_block_under():
    block = bot.blockAt(bot.players[username].entity.position.offset(0, -1, 0))
    bot.chat(f"Block under you is {block.displayName} in the {block.biome.name} biome")
    print(block)
