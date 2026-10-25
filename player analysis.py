class Player:
    def __init__(self,name,points,assists,rebounds):
        self.name = name
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

    def display_info(self):
        print("name",self.name)
        print("points",self.points)
        print("assists",self.assists)  
        print("rebounds",self.rebounds)

def calculate_total_statistics(player):
    return player.points + player.assists + player.rebounds

def get_average_points(players):
    total = 0
    for player in players:
        total += player.points
    return total/len(players)


player1 = Player("curry",23,4,6)
player2 = Player("tonka",56,4,5)
player3 = Player("vindee",19,6,9)
player4 = Player("james",30,5,8)
player5 = Player("harden",45,3,1)
player6 = Player("kevin",34,6,9)

players = [player1,player2,player3,player4,player5,player6]

highest_player = max(players,key = lambda player:player.points)
lowest_player = min(players,key = lambda player:player.points)

search_player = input("enter the name of the player you want to look up : ")
for player in players:
    if player.name.lower() == search_player.lower():
      print(f"the player scored {player.points} points")
      print(f"the player scored {player.assists} assists")
      print(f"the player scored {player.rebounds} rebounds")
      break
else:
    print("the player you are searching for is not found!!!") 
print("the player with the highest points is : ",highest_player.name)       
print("the player with te lowest points is : ",lowest_player.name)
player1.display_info()
player2.display_info()
player3.display_info()
player4.display_info()
player5.display_info()
player6.display_info()

print("the average points of all the players is : ",get_average_points(players))
print(f"the total stats of {player1.name} is : ",calculate_total_statistics(player1))
print(f"the total stats of {player2.name} is : ",calculate_total_statistics(player2))
print(f"the total stats of {player3.name} is : ",calculate_total_statistics(player3))
print(f"the total stats of {player4.name} is : ",calculate_total_statistics(player4))
print(f"the total stats of {player5.name} is : ",calculate_total_statistics(player5))
print(f"the total stats of {player6.name} is : ",calculate_total_statistics(player6))
