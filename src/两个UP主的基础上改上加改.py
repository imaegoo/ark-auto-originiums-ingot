# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
auto_setup(__file__)
a=0#运行步数
b=0#判断关卡搜索次数
c=0#投资次数计数
def panduanguoguan():
    while not exists(Template(r"tpl1641989217172.png", record_pos=(-0.366, 0.15), resolution=(1440, 810))):#判断过关
        sleep(4.0)#没有成功通过就等4秒，然后继续循环找成功通过
    else:
        sleep(2.0)#找到了之后，为了防止在“成功通关”这四个字从画面左边飞到画面内的瞬间识别到并立刻进行点击而设置的一个等待时间。（因为计算机执行）
    touch((1000,490))#识别到了点击一下
    sleep(1.0)
    while not exists(Template(r"tpl1641989331329.png", record_pos=(0.296, 0.07), resolution=(1440, 810))):#判断有没有这个图片
        swipe((670,500),vector=[-0.3,0])#判断没有，就自右往左滑动屏幕，移到右边，移完回去继续判断图片
    else:
        touch(Template(r"tpl1641989331329.png", record_pos=(0.296, 0.07), resolution=(1440, 810)))#判断到了就点它
    sleep(1.0)
    touch(Template(r"tpl1641989346223.png", record_pos=(0.339, 0.147), resolution=(1440, 810)))
    sleep(1.0)
def likai():
    touch((45,30))
    sleep(1.0)
#第二次探索如果卡主，可以适当将这里的sleep时间增加一点，比如sleep(3.0)，sleep可以理解为等待一段时间的意思
    touch(Template(r"tpl1641990570636.png", record_pos=(0.412, -0.018), resolution=(1440, 810)))
    sleep(2.0)
#这个对象likai()里的这些sleep时间都可以适当改一下，改到适合自己模拟器运行加载速度的等待时间
    touch(Template(r"tpl1641990587770.png", record_pos=(0.159, 0.106), resolution=(1440, 810)))
    sleep(5.0)
    touch((700,730))#等一段时间点击画面进入下一个结算的界面
    sleep(6.0)
    touch((700,730))#等一段时间点击画面进入下一个结算的界面，点完这次应该就会回到肉鸽主菜单
    sleep(3.0)
    touch((1300,650))
    sleep(3.0)#对，就是这个，靠在一起了应该可以看到吧
def kaishi():
    touch((1300,650))
#可以回到肉鸽主界面但不会进行下一次探索的，请修改likai()对象里面最下面的那个sleep时间'''
    while not exists(Template(r"tpl1641990883595.png", threshold=0.8, record_pos=(0.203, 0.063), resolution=(1440, 810))):
#精二高级的山比较稳定过关，所以选了这个分队'''
        swipe((670,500),vector=[-0.1861, 0.007])
    else:
        touch(Template(r"tpl1641990883595.png", threshold=0.8, record_pos=(0.203, 0.063), resolution=(1440, 810)))
#有需要的就把这两个突击战术分队的图片换成自己想要的分队吧，用左侧Airtest辅助窗里的功能就可以截图生成自己的代码了。'''
        touch(Template(r"tpl1641991004571.png", record_pos=(0.287, 0.182), resolution=(1440, 810)))
    sleep(1.0)
    touch(Template(r"tpl1641991034647.png", record_pos=(0.11, 0.062), resolution=(1440, 810)))
    touch(Template(r"tpl1641991004571.png", record_pos=(0.287, 0.182), resolution=(1440, 810)))
    sleep(2.0)
    touch((390,600))#点击第一张招募券下面的招募按钮的坐标。
    sleep(1.0)
    
    swipe((670,500), vector=[-0.1223, 0.0019]) #山在第三列故加此动作，如果山在前两列请把这一行删掉
    
    sleep(1.0)


    
    if exists(Template(r"tpl1641991518242.png", record_pos=(0.051, -0.149), resolution=(1440, 810))):#判断画面内有没有山，有就选，没有就执行else:后面的内容
        touch(Template(r"tpl1641991518242.png", record_pos=(0.051, -0.149), resolution=(1440, 810)))
        sleep(2.0)
        touch((1250,750))
        sleep(3.0)
    else:#上面if是选择自己的山，else下面的部分是选择用助战
        touch((1220,30))
        while not exists(Template(r"tpl1641991335442.png", threshold=0.9000000000000001, target_pos=6, record_pos=(-0.222, 0.222), resolution=(1440, 810))):#因为有时候刷新到的山在第三列，招募按钮在右边画面外，所以设置的一个判断。
            touch((1300,30))
            while not exists(Template(r"tpl1641991147628.png", record_pos=(0.025, -0.117), resolution=(1440, 810))):
                touch((1300,30))
            else:
                pass
        else:
            touch(Template(r"tpl1641991335442.png", threshold=0.9000000000000001, target_pos=6, record_pos=(-0.222, 0.222), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"tpl1641991373517.png", record_pos=(0.157, 0.124), resolution=(1440, 810)))
        sleep(2.0)
    while not exists(Template(r"tpl1641991518242.png", record_pos=(0.051, -0.149), resolution=(1440, 810))):#判断画面是否在那个招到了干员的画面。
        sleep(1.0)
    else:
        sleep(1.0)
    touch((700,730))#上面判断到了在那个画面再点击一下屏幕进入下一步。
    sleep(1.0)
    touch((700,600))#点击第二张招募券下面的招募按钮的坐标。
    touch(Template(r"tpl1641991636323.png", record_pos=(0.256, 0.249), resolution=(1440, 810)))
    sleep(1.0)
    touch(Template(r"tpl1641991650485.png", record_pos=(0.158, 0.106), resolution=(1440, 810)))
    sleep(1.0)
    touch((1000,600))#点击第三张招募券下面的招募按钮的坐标。
    touch(Template(r"tpl1641991636323.png", record_pos=(0.256, 0.249), resolution=(1440, 810)))
    sleep(1.0)
    touch(Template(r"tpl1641991650485.png", record_pos=(0.158, 0.106), resolution=(1440, 810)))
    sleep(1.0)
    touch(Template(r"tpl1641991718574.png", record_pos=(0.441, -0.006), resolution=(1440, 810)))
    sleep(4.0)
    b=0
def xuanren():
    if exists(Template(r"tpl1641994682261.png", record_pos=(-0.32, -0.146), resolution=(1440, 810))):#判断行动选干员界面有没有山
        pass#有就pass不管
    else:
        touch((250,190))#没有就执行这段选山和选择技能。
        sleep(1.0)
        touch((680,160))
        sleep(1.0)
        touch((200,600))
        sleep(1.0)
        touch((1270,760))
def shijian():
    touch(Template(r"tpl1641987478502.png", record_pos=(0.395, 0.096), resolution=(1440, 810)))
    sleep(4.0)
    touch((1190,460))#这个点击的坐标可以在只有一个或两个选项的时候点击到最下面选项的位置。
    sleep(3.0)
    if exists(Template(r"tpl1642038786944.png", record_pos=(0.435, 0.071), resolution=(1440, 810))):#这里是针对不期而遇里有三个选项的情况进行确认。
        touch(Template(r"tpl1642038786944.png", record_pos=(0.435, 0.071), resolution=(1440, 810)))
    else:
        touch((1190,460))
    sleep(2.0)
    touch(Template(r"tpl1641987560872.png", threshold=0.8, record_pos=(0.435, 0.096), resolution=(1440, 810))) 
    sleep(4.0)
    touch(Template(r"tpl1641987578489.png", record_pos=(0.0, 0.232), resolution=(1440, 810)))
    sleep(3.0)
    b=0
    swipe((670,500),vector=[-0.3878, 0.0048])

def buqieryu():
    touch(Template(r"tpl1642165550078.png", rgb=True, record_pos=(0.102, 0.026), resolution=(1440, 810)))
    shijian()
def buqieryu2():
    touch(Template(r"tpl1642309607542.png", record_pos=(0.217, 0.113), resolution=(1440, 810)))
    shijian()
def mujianyuxing():
    touch(Template(r"tpl1642760254220.png", record_pos=(0.217, -0.048), resolution=(1440, 810)))
    shijian()
def xunshouxiaowu():
    touch(Template(r"tpl1641987600343.png", record_pos=(0.156, -0.022), resolution=(1440, 810)))
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    xuanren()
    sleep(1.0)
    touch(Template(r"tpl1641988492692.png", record_pos=(0.322, 0.242), resolution=(1440, 810)))
    sleep(9.0)
    touch((1239,65),duration=0.2)

    sleep(3.0)
    swipe(Template(r"tpl1641988605026.png", record_pos=(0.457, 0.237), resolution=(1440, 810)),(1180,400),duration=2)#拖干员到位置，duration是拖动过程的时间，可以自行设定适当的时间防止模拟器卡顿没下到干员，单位秒，默认是0.5秒的，有人反映下干员太快就加了这个。
    sleep(1.0)
    swipe((1180,400),(1380,400))#设置朝向，这里也可以加duration=来设定拖动时间，招着上面的样子写出来代码就好。
    sleep(6.0)
    touch((1100,410))#点山
    sleep(2.0)#如果连点山和开技能之间都卡了，那这里的等待时间自行增加吧。
    touch((1000,490))#开山技能
    panduanguoguan()
    b=0
def lipaoxiaodui():#注释参考xunshouxiaowu()里的注释
    touch(Template(r"tpl1641991796991.png", record_pos=(-0.195, 0.029), resolution=(1440, 810)))
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    xuanren()
    sleep(1.0)
    touch(Template(r"tpl1641988492692.png", record_pos=(0.322, 0.242), resolution=(1440, 810)))

    sleep(9.0)
    touch((1239,65),duration=0.2)#点击加速
    sleep(1.0)
    swipe(Template(r"tpl1641988605026.png", record_pos=(0.457, 0.237), resolution=(1440, 810)),(575,386),duration=2)#拖干员到位置
    sleep(1.0)
    swipe((560,382),(1380,400))#设置朝向
    sleep(6.0)
    touch((455,364))#点山
    sleep(2.0)
    touch((1000,490))#开山技能
    panduanguoguan()
    b=0
def yiwai():#注释参考xunshouxiaowu()里的注释
    touch(Template(r"tpl1641998962031.png", record_pos=(-0.196, 0.031), resolution=(1440, 810)))
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    xuanren()
    sleep(1.0)
    touch(Template(r"tpl1641988492692.png", record_pos=(0.322, 0.242), resolution=(1440, 810)))
    sleep(9.0)
    touch((1239,65),duration=0.2)#点击加速
    sleep(3.0)
    swipe(Template(r"tpl1641988605026.png", record_pos=(0.457, 0.237), resolution=(1440, 810)),(806,370),duration=2)#拖干员到位置
    sleep(1.0)
    swipe((806,370),(1380,400))#设置朝向
    sleep(1.0)
    sleep(5.0)
    touch((715,363))#点山
    sleep(2.0)
    touch((1000,490))#开山技能
    panduanguoguan()
    b=0
def yuchongweiban():#注释参考xunshouxiaowu()里的注释
    touch(Template(r"tpl1641994030492.png", record_pos=(-0.196, 0.03), resolution=(1440, 810)))
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    xuanren()
    sleep(1.0)
    touch(Template(r"tpl1641988492692.png", record_pos=(0.322, 0.242), resolution=(1440, 810)))
    sleep(9.0)
    touch((1239,65),duration=0.2)#点击加速
    sleep(1.0)
    swipe(Template(r"tpl1641988605026.png", record_pos=(0.457, 0.237), resolution=(1440, 810)),(667,432),duration=2)#拖干员到位置
    sleep(1.0)
    swipe((667,432),(1380,400))#设置朝向
    sleep(6.0)
    touch((575,411))#点山
    sleep(1.0)
    touch((930,450))#开山技能
    panduanguoguan()
    b=0
def shandian():
    sleep(1.0)
    touch((1290,600))
    sleep(1.0)
    c=0
    if exists(Template(r"tpl1641989654147.png", record_pos=(-0.105, -0.19), resolution=(1440, 810))):
        touch(Template(r"tpl1641989721200.png", record_pos=(-0.103, -0.19), resolution=(1440, 810)))
        sleep(1.0)
        touch(Template(r"tpl1641989745261.png", record_pos=(-0.074, -0.037), resolution=(1440, 810)))
        sleep(1.0)
        while c<5:#为解决投完了身上的源石锭还没到投资受限的情况而设置的判断（运气好试过几次17颗源石锭投完了还能继续投就卡住了的情况。）
            if not exists(Template(r"tpl1641989989616.png", threshold=0.9000000000000001, record_pos=(0.113, -0.04), resolution=(1440, 810))):
                touch((1100,560),times=40)
                c+=1
            else:
                sleep(1.0)
                c=5
        else:
            c=0
            likai()
    else:
        sleep(2.0)
        likai()
    kaishi()
    b=0
def panduanguanqia():
    sleep(2.0)
    
    
    if exists(Template(r"tpl1642309756949.png", record_pos=(0.215, 0.005), resolution=(1440, 810))):
        touch(Template(r"tpl1642309756949.png", record_pos=(0.215, 0.005), resolution=(1440, 810)))
        shandian()
    
    elif exists(Template(r"tpl1642309539033.png", record_pos=(0.216, 0.112), resolution=(1440, 810))):
        buqieryu2()
        
    elif exists(Template(r"tpl1642760254220.png", record_pos=(0.217, -0.048), resolution=(1440, 810))):
        mujianyuxing()
        
    
    elif exists(Template(r"tpl1641987600343.png", threshold=0.9000000000000001, rgb=False, record_pos=(0.156, -0.022), resolution=(1440, 810))):
        xunshouxiaowu()
    elif exists(Template(r"tpl1641991796991.png", threshold=0.9000000000000001, rgb=False, record_pos=(-0.195, 0.029), resolution=(1440, 810))):
        lipaoxiaodui()
    elif exists(Template(r"tpl1641998962031.png", threshold=0.9000000000000001, rgb=False, record_pos=(-0.196, 0.031), resolution=(1440, 810))):
        yiwai()
    elif exists(Template(r"tpl1641994030492.png", threshold=0.9000000000000001, rgb=False, record_pos=(-0.196, 0.03), resolution=(1440, 810))):
        yuchongweiban()
        
    
    
    
    
    elif b>1:#由于识别图片，经常搜索不到不期而遇，这里是判断关卡两次没搜索到后运行的代码。
        touch((900,360))#点击固定的几个点
        sleep(1.0)
        touch((900,120))
        sleep(1.0)
        touch((900,440))
        sleep(1.0)
        touch((900,200))
        sleep(1.0)
        touch((900,280))
        if exists(Template(r"tpl1642143362809.png", threshold=0.8, record_pos=(0.247, -0.144), resolution=(1440, 810))):#判断最终选择了什么关卡，然后执行相应的对象。由于战斗分支通常不会因搜索不到而触发反复判断的BUG，所以这里不对战斗关卡分支的图片进行判断。
            shijian()
        
        elif exists(Template(r"tpl1642172966906.png", threshold=0.8, record_pos=(0.247, -0.145), resolution=(1440, 810))):
            shijian() 
        elif exists(Template(r"tpl1642255403039.png", threshold=0.8, record_pos=(0.247, -0.144), resolution=(1440, 810))):
            shandian()
        else:
            pass
kaishi()#脚本从这里开始运行
while a<100:
    panduanguanqia()
    a+=1
    b+=1
else:
    pass
