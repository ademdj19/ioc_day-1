inputs = open("Beginnings-main.txt","r").read()
unsafe_rooms = map(int,inputs.split("\n"))
sum_of_all_rooms = 494550
sum_of_unsafe_rooms = sum(unsafe_rooms)
sum_of_safe_rooms = sum_of_all_rooms - sum_of_unsafe_rooms
print(sum_of_safe_rooms)