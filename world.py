from action import Bot
world = [
    [0, 0, 0, 0 , 0, 0, 0, 0],
    [0, 0, 0, 0 , 0, 0, 0, 0],
    # [0, 6, 0, 0 , 0, 0, 0, 0],
    [0, 1, 0, 0 , 0, 0, 0, 0],
    [0, 3, 0, 0, 0 , 0, 0, 0],
    [0, 4, 0, 0 ,0 , 0, 0, 0],
    [0, 2, 0, 0 ,0 , 0, 0, 0],
    [0, 7, 0, 0 ,0 , 0, 0, 0],
    
]
# print(Bot(world).getPosition(1, 2))
bot = Bot(world)
# bot.mov(3)
# bot.grab()
# # bot.placeOnBox(1)
# print(bot.placeOnTable())
# bot.clear(3)
print(bot.getWorld())
print("=================================")

bot.swap(3, 2)

print(bot.getWorld())


# print(bot.FirstItemInCol(3))
# print(bot.onTable(2))
# bot.placeBoxOnTopanother(2, 3)
# bot.boxUnderAnother(2, 3)
# bot.sortStack([1,3,4,2,7], "descending")
# bot.mov(4)
# bot.grab()
# # bot.placeOnBox(1)
# print(bot.placeOnTable())
# bot.mov(9)
# bot.grab()
# bot.placeOnBox(7)
# (bot.getSinglePosition(2))
# bot.placeOnTable()
# print(bot.clear(9))


    