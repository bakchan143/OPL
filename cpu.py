registers={
    "R0":0,
    "R1":0,
    "R2":0,
    "R3":0


}
program = [
   "LOAD R0,10",
    "LOAD R1,10",
    "CMP R0,R1"
]
pc=0
equal=False
while pc < len(program):#4 = 0,1,2,3
    instruction = program[pc]
    if instruction=="HALT":
        print("HALT")
        break
    operator, reminder= instruction.split(maxsplit=1) 
    if operator=="LOAD":
        register, value= reminder.split(",")
        registers[register]=int(value)
    elif operator=="ADD":
        register, value1,value2= reminder.split(",")
        registers[register]=registers[value1]+registers[value2]
    elif operator=="SUB":
        register, value1,value2= reminder.split(",")
        registers[register]=registers[value1]-registers[value2]
    elif operator=="CMP":
        value1,value2= reminder.split(",")
        equal= registers[value1]==registers[value2]
            
            
    pc+=1

print(registers)

