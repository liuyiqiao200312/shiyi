"""作者：刘逸乔      程序目标：实现RPSLS游戏"""
import random
a=random.randint(0,4)
def number_to_name(a):
    if a==0:
        a=str("石头")
    if a==1:
        a=str("史波克")
    if a==2:
        a=str("布")
    if a==3:
        a=str("蜥蜴")
    if a==4:
        a=str("剪刀")
    return(a)#定义数字到名字的转变
def name_to_number(a):
    if a==("石头"):
        a=float(0)
    if a==("史波克"):
        a=float(1)
    if a==("布"):
        a=float(2)
    if a==("蜥蜴"):
        a=float(3)
    if a==("剪刀"):
        a=float(4)
    return(a)#定义东西到数字的转变
def rpsls(player_choice):
    a=name_to_number(player_choice)#将输入东西的转为数
    b=random.randint(0,4)
    if a==0 and b==[3 or 4]:
        c=str(number_to_name(b))#将电脑的数转为名
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("你赢了")
    if a==1 and b==[4 or 0]:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("你赢了")
    if a==2 and b==[0 or 1]:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("你赢了")
    if a==3 and b==[1 or 2]:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("你赢了")
    if a==4 and b==[2 or 3]:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("你赢了")
    if a==b:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("平局")
    else:
        c=str(number_to_name(b))
        print("----------------")
        print("您的选择是%s"%player_choice)
        print("机器的选择是%s"%c)
        print("您输了")
    return(player_choice)
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name in ("石头","史波克","布","蜥蜴","剪刀") :
    rpsls(choice_name)
else:
    print("Error: No Correct Name")#如果不是
    


        
    
        
    
    
    
