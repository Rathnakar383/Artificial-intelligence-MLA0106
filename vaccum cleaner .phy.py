def vacuum_cleaner():
    rooms = {'A': 'dirty', 'B': 'dirty'}
    print("Initial:", rooms)

    for room in rooms.keys():
        if rooms[room] == 'dirty':
            print(f"Cleaning room {room}")
            rooms[room] = 'clean'
        print(f"Room {room} is now {rooms[room]}")

    print("Final state:", rooms)

vacuum_cleaner()
