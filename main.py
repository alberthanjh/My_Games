import pygame as pg
from source.main import main
import os
import random
import re
import json

l=[]
path="source\\data\\map\\"
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        path1=os.path.join(root, name)
        if "level_0" not in path1:
            l.append(path1)

#僵尸名
zombie_names=["Zombie","ConeheadZombie","BucketheadZombie","FlagZombie","NewspaperZombie"]
to_hard_zombies=["BucketheadZombie","NewspaperZombie"]
news_times=0
#随机数
for i in l:
    with open(i,"r") as f:
        js=json.loads(f.read())
    #加载
    #获取僵尸信息
    k=0#遍历次数
    for dictory in js["zombie_list"]:#遍历僵尸列表
        dictory["map_y"]=random.randint(0,4)
        '''
        zombie_name=random.choice(zombie_names)
        if k<=5:#开局保护机制
            while zombie_name in to_hard_zombies:
                zombie_name=random.choice(zombie_names)
        if news_times>4:#二爷次数削弱
            while zombie_name == "NewspaperZombie":
                zombie_name=random.choice(zombie_names)
        if zombie_name == "NewspaperZombie":#二爷次数增加
            news_times+=1
        '''
        if k%3==0:
            zombie_name="Zombie"
        elif k%3==1:
            r=random.randint(1,5)
            if r == 1:
                zombie_name="NewspaperZombie"
            else:
                zombie_name="ConeheadZombie"
        else:
            zombie_name=random.choice(zombie_names)
        dictory["name"]=zombie_name
        js["zombie_list"][k]=dictory
        k+=1
    js2=json.dumps(js)
    with open(i,"w") as f:
        f.write(js2)

    l.remove(i)


if __name__=='__main__':

    main()
    pg.quit()