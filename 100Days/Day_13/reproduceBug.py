from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

dice_num_fixed = randint(0, 5)
print(dice_images[dice_num_fixed])