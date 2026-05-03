import random
import math

def game():
    while True:
        start_game = input("Start Game? y/n: ").lower()

        if start_game not in ['y', 'n']:
            print("choose valid answer y/n")
            continue

        if start_game == 'y':
            print("Game starting")
        else:
            print("Game ended")
            break

        items = ['Key', 'Map', 'Sword', 'Coin', 'Potion']
        inventory = []
        points = 0
        energy = 100
        moves = 0

        number = random.randint(1, len(items))

        rooms = {
            "forest": list(random.sample(items, number)),
            "cave": list(random.sample(items, number)),
            "river": list(random.sample(items, number)),
            "tower": list(random.sample(items, number)),
            "treasure_room": list(random.sample(items, number))
        }

        room = 'forest'   

        print(f"First Room: Forest, You have found items: {rooms['forest']} \n")

        while True:

            if energy <= 0:
                print("You lost (no energy)")
                break

            next_action = input("Next Action (Move, Take, Inventory, Status, Quit): ").lower()

            if next_action not in ['move', 'take', 'inventory', 'status', 'quit']:
                print("Choose valid answer (Move, Take, Inventory, Status, Quit)")
                continue


            if next_action == 'take':
                for i in rooms[room].copy():  
                    if i == 'Key':
                        points += 10
                    if i == 'Map':
                        points += 8
                    if i == 'Sword':
                        points += 7
                    if i == 'Coin':
                        points += 5
                    if i == 'Potion':
                        points += 6

                    inventory.append(i)
                    rooms[room].remove(i)  

                print("Items taken")
                continue

            if next_action == 'move':
                print("Moving.. \n")

                next_room = input("Choose Next Room: ").lower()

                if next_room not in ['cave', 'river', 'tower', 'treasure_room']:
                    print('Choose Valid Answer')
                    continue

                energy -= random.randint(5, 15)
                moves += 1

                if moves % 3 == 0:
                    bonus = math.ceil(points / 10)
                    energy += bonus

                if next_room == 'treasure_room':
                    if ('Key' in inventory and 'Map' in inventory and points >= 20 and len(inventory) >= 3):
                        print("Win")
                        break
                    else:
                        print("Can't enter treasure room yet")
                        continue

                room = next_room   

                cave = rooms['cave']
                river = rooms['river']
                tower = rooms['tower']

                if next_room == 'cave':
                    print(f"Cave Room, You have found items: {cave}")

                elif next_room == 'river':
                    print(f"River Room, You have found items: {river}")

                elif next_room == 'tower':
                    print(f"Tower Room, You have found items: {tower}")

                continue

            if next_action == 'inventory':
                print(inventory)
                print(f"Items: {len(inventory)}")
                continue

            if next_action == 'status': 
                print(f"Current room: {room}")
                print(f"Points: {points}")
                print(f"Energy: {energy}")
                print(f"Inventory size: {len(inventory)}")
                continue

            if next_action == 'quit':
                break


game()