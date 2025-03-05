line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input()

position_lower = position.lower()

if position_lower[0] == "a":
  if position_lower[1] == "1":
    line1[0] = "X"
  elif position_lower[1] == "2":
    line2[0] = "X"
  elif position_lower[1] == "3":
    line3[0] = "X"
elif position_lower[0] == "b":
  if position_lower[1] == "1":
    line1[1] = "X"
  elif position_lower[1] == "2":
    line2[1] = "X"
  elif position_lower[1] == "3":
    line3[1] = "X"
elif position_lower[0] == "c":
  if position_lower[1] == "1":
    line1[2] = "X"
  elif position_lower[1] == "2":
    line2[2] = "X"
  elif position_lower[1] == "3":
    line3[2] = "X"

print(f"{line1}\n{line2}\n{line3}")