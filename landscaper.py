landscaper = {"money":0, "tool":0}

tools=[
    {"name":"teeth", "earning": 1, "cost":0},
    {"name":"rusty scissors", "earning": 5, "cost":5}
]

def cut_grass():
    tool=tools[landscaper["tool"]]
    print (f"landscaped with {tool['name']} and make {tool['earning']}")
    landscaper["money"] +=tool["earning"]

def stats():
    tool=tools[landscaper["tool"]]
    print(f"You have {landscaper['money']} and are using a {tool['name']}")
    
def upgrade():
    next_tool=tools[landscaper["tool"]+1]
    if (next_tool==0):
        print("no more tool")
        return 0
    if (landscaper["money"]<next_tool["cost"]):
        print("not enough to upgrade")
        landscaper["money"] -=next_tool("cost")
        landscaper["tool"] +=1
        
def win():
    if(landscaper["tool"]==1 and landscaper["money"]==100):
        print("win")
        return True
    return False

## building the loop
while (True):
    
    i=input("[1] cut grass [2] check stats [3] updrade [4] quit")
    i==int(i)
    if (i==1):
        cut_grass()
    if (i==2):
        check_stats()
    if (i==3):
        upgrade()
    if (i==4):
        print("quit game")
        break
    if (win()):
        break
    