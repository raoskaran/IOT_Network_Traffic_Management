import pandas as pd

data   = "./data.csv"

df     = pd.read_csv(data)
info   = df["Info"]

#info   = [info[0],info[1],info[2]]

sport,dport,flag,seq,ack,win,length,allInf  = [],[],[],[],[],[],[],[]

l = len(info)

for i in range(l):
    print('\nCount = ',i)
    row    = info[i].split(" ")
    row[:] = (value for value in row if value != "")    #removes all whitespace elements
    #print(row)
    if(row[0][0]=='['):                             #reused ports message
        port = row[3][7:]
        for trash in range(4):
            row.remove(row[trash])
        row.insert(0,port)

    if(row[4][0]!= 'S'):                            #not seq no
        row[3] = row[3] + row[4]
        row.remove(row[4])
    print(row)
    #print(row[4])
    row[4] = row[4][4]                              #seq no
    if(row[5][0] == 'A'):                              #ack
        row[5] = row[5][4:]
    else:
        row.insert(5," ")
    row[6] = row[6][4:]                             #win
    row[7] = row[7][4:]                             #len
    
    sport.append(row[0])
    dport.append(row[2])
    flag.append(row[3])
    seq.append(row[4])
    ack.append(row[5])
    win.append(row[6])
    length.append(row[7])

print("sport ",len(sport))  #sport  116954
print("dport ",len(dport))  #dport  116954
print("flag ",len(flag))    #flag  116954
print("seq ",len(seq))      #seq  116954
print("ack ",len(ack))      #ack  116954
print("win ",len(win))      #win  116954
print("len ",len(length))   #len  116954

df["Src_Port"] = sport
df["Dest_Port"] = dport
df["Flag"]  = flag
df["Seq"]   = seq
df["Ack"]   = ack
df["Win"]   = win
df["Len"]   = length

df.to_csv(data)