print("3 Ways to use concatenation are:\n")

print("1) \"String\" + Variable:")
var1 = "Monsters"
print("   a.Shrek School Academy are for " + var1)
print("   b.We " + var1 + " will kill you")
print("   c." + var1 + " are here!")
print("\n")
print("2) \"String {}\".format(Variable)")
var2 = "Beasts"
print("   a.Shrek School Academy are for {}".format(var2))
print("   b.{} are here to save us".format(var2))
print("   c.BANK ROBBER:\"Oh no, it's these {}, RUN!\" ".format(var2))
print("\n")
print("3) f\"String {Variable}\"")
var3 = "Animals"
print("   a."+ f"Kill these {var3}")
print("   b."+ f"We have to Kill these {var3} otherwise it we'll die")
print("   c."+ f"{var3} are evil")