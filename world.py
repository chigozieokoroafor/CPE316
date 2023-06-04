from action import Bot
world = [
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 1 , 0, 0, 0, 0],
    [0, 0, 0, 3 , 0, 0, 0, 0],
    [0, 0, 0, 2 , 7, 0, 9, 0],
]
# print(Bot(world).getPosition(1, 2))
bot = Bot(world)
bot.mov(1)
bot.grab()
bot.placeOnTable()
print(bot.getWorld())


    