# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f"Player: {self.name} \n{self.current_room}"


# player = Player("Lisa", "outside")

# print(player)