from human import Human
from card import Card

vignesh = Human("Vigneshwaran", True)
praveen = Human("Praveenkumar", True)
# print(vignesh.name)
# vignesh.think()

vigneshCreditCard = Card("5467937493830", "2024-04-22", "123", "VIGNESHWARAN")
print(vigneshCreditCard.isExpired())
print(vigneshCreditCard.expiryDays())