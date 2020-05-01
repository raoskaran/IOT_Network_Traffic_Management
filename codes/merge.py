import pandas as pd

tcp        = "./Tcp"
udp       = "./Udp"
normal = "./normal"

dft = pd.read_csv(tcp)
dfu = pd.read_csv(udp)
dfn = pd.read_csv(normal)

yay = pd.concat([dft, dfu, dfn], ignore_index=True)

print(yay.shape)

with open('./dataset.csv', 'w', encoding='utf-8') as f:
    yay.to_csv(f, index=False)