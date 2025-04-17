data={"b":20,"a":35}
data["b"]=-data["b"]
data["c"]=40
data.pop("b",None)
print(sorted(data.keys()))
