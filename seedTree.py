import networkx as nx 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_excel("PIN Yield Improvement 01302019.xlsx", sheet_name = "Run Matrix")
#df["CrystalName"] = df.apply(lambda row: row.FurnaceID + "-" + str(row.Run), axis= 1)

df = df[1:]
df = df.sort_values("Xtl ID")
g = nx.from_pandas_edgelist(df,target="Xtl ID", source = "Seed",create_using = nx.DiGraph)

df = df.set_index("Xtl ID")
nodeAtts = []




for node in g.nodes():
    try:
        Yield = df["Result"].loc[node]
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
pos = nx.drawing.nx_agraph.graphviz_layout(g, prog="dot")
nx.draw(g,pos, arrows=True, with_labels = True,node_color= colorlist, font_weight = 'bold',)
plt.show()
