st = []
name_list=[]
count  = 0
while True:
if count == 3:
	break
#输入
dict = {}
#for i in list:
#   name_list.append(i.get("name"))
	name = input("请输入你的名字")
	age = int(input("请输入你
	sex = input("请输入你的性别")
 18     qq = int(input("请输入你的qq号"))
 19     weight = float(input("请输入你的体重"))
 20     #字典赋值 
 21     if name not in name_list:
 22         dict["name"] = name
 23         dict["age"] = age
 24         dict["sex"] = sex
 25         dict["qq"] = qq
 26         dict["weight"] = weight
 27         #list = [{}]
 28         #int float str bool list tuple dictionary
 29         list.append(dict)
 30         name_list.append(name)#一定要记录
 31         print(list)
 32         count+=1
 33     else:
 34         print("名字重了")
 35 age_sum =0
 36 #遍历
 37 #list =[{},{},{}]
 38 for i in list:
 39     age_sum = age_sum+i.get("age")
 40     print(i)
 41 print("年龄的平均值是%0.2f"%(age_sum/len(list)))

