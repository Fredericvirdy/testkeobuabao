print("Nhap keo, bua, bao ")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "bua"
if computer == 1:
    computer = "bao"
if computer == 2:
    computer = "keo"

print("---")    
print("you choose:" +player )
print("computer chooses:" + computer)
print("---")
