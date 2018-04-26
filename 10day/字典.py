a = {"name":"刘明松","age":24,"height":175,"group":"汉"}
print(a)
a["address"] = "山东"
print(a)
a.setdefault("zhangxiang","完美")
print(a)
#a.pop("age")
#a.popitem()
#del a["height"]
print(a)
a["name"] = "林枫秀"
print(a)
print(a["name"])
print(a.get("ame"))
a2 = {"name":"王五","liuliuliu":666}
a.update(a2)
print(a)
print(a.keys())
print(a.values())
print(a.items())
