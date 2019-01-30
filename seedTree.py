import networkx as nx 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_excel("SeedTest.xlsx")
df["CrystalName"] = df.apply(lambda row: row.FurnaceID + "-" + str(row.Run), axis= 1)



g = nx.from_pandas_edgelist(df,"CrystalName", "Seed Crystal")

df = df.set_index("CrystalName")
nodeAtts = []

for node in g.nodes():
    try:
        Yield = df["Yield"].loc[node]
    except:
        Yield = "Single"

    if Yield == "Single":
        color = "g"
    elif Yield == "Poly":
        color = "r"
    elif Yield == "Partial":
        color = "y"
    
    nodeAtts.append((node, {"Yield": color}))


g.add_nodes_from(nodeAtts)

colorlist = list(nx.get_node_attributes(g,"Yield").values())
nx.draw_kamada_kawai(g, with_labels = True,node_color= colorlist, font_weight = 'bold')
plt.show()
