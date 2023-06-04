from action import Bot
world = [
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 3, 0, 0, 0 , 0, 0, 0],
    [0, 4, 0, 0 ,0 , 0, 0, 0],
    [0, 2, 0, 0 ,0 , 0, 0, 0],
    [0, 7, 0, 0 ,0 , 0, 0, 0],
]
# print(Bot(world).getPosition(1, 2))
bot = Bot(world)
# bot.mov(7)
# bot.grab()
# bot.placeOnBox(1)
# bot.placeOnTable()
# bot.clear(3)
print(bot.getWorld())
print("=================================")
bot.mov(9)
bot.grab()
bot.placeOnBox(7)
(bot.getSinglePosition(2))
# bot.placeOnTable()
# print(bot.clear(9))
# bot.swap(2, 3)
# print(bot.FirstItemInCol(3))
# print(bot.getWorld())

    