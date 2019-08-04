def TowersOfHanoi(n, frompeg, topeg, auxpeg):
  num = int(n)
  if(num == 1):
    print("Move disk", n,  "from", frompeg, "to", topeg)
    return
    
  # move the top n - 1 disks from A to B using C as auxiliary
  TowersOfHanoi(num-1, frompeg, auxpeg, topeg)

  # move the rest of the disks from A to C
  print("Move disk", n,  "from", frompeg, "to", topeg)

  # move the n - 1 disks form B to C using A as auxiliary
  TowersOfHanoi(num-1, auxpeg,topeg, frompeg)

user = input("How many rings are there? ")

TowersOfHanoi(user, "A", "B", "C")

