landscaper = {"money":0, "tool":0}

tools=[
    {"name":"teeth", "earning": 1, "cost":0},
    {"name":"rusty scissors", "earning": 5, "cost":5},
    {"name":"old timely push lawnmower", "earning":50, "cost":25},
    {"name":"battery-powered lawnmower", "earning":100, "cost": 250},
    {"name":"starving students", "earning":250, "cost":500}
]

def cut_grass():
    tool=tools[landscaper["tool"]]
    print (f"landscaped with {tool['name']} and make {tool['earning']}")
    landscaper["money"] +=tool["earning"]

def stats():
    tool=tools[landscaper["tool"]]
    if (landscaper["money"]>=5 and landscaper["money"]<25):
        print("you can buy scissors")
    if (landscaper["money"]>=25 and landscaper["money"]<250):
        print("you can buy old timely push lawnmower")
    if (landscaper["money"]>=250 and landscaper["money"]<500):
        print("you can buy a fancy battery-powered lawnmower")
    if (landscaper["money"]>=500):
        print("you can hirng a team")
    print(f"You have {landscaper['money']} and are using a {tool['name']}")
    
def upgrade():
    next_tool=tools[landscaper["tool"]+1]
    if (next_tool==None):
        print("no more tool")
        return 0
    if (landscaper["money"]<next_tool["cost"]):
        print("not enough to upgrade")
    landscaper["money"] -=next_tool["cost"]
    landscaper["tool"] +=1
    print(f"You have upgraded to {next_tool}")
        
def win():
    if(landscaper["tool"]==4 and landscaper["money"]==1000):
        print("win")
        return True
    return False

## building the loop
while (True):
    
    i=input("[1] cut grass [2] check stats [3] updrade [4] quit")
    i=int(i)
    if (i==1):
        cut_grass()
    if (i==2):
        stats()
    if (i==3):
        upgrade()
    if (i==4):
        print("quit game")
        break
    if (win()):
        break
    