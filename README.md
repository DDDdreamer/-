# HappyThirteenWater
## 徽章
![](https://img.shields.io/badge/python-3.7-green)<br>
![](https://img.shields.io/badge/HappyThirTeenWater-v1.0.0-brightgreen)<br>
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0d5f099c86ee403591c3132b75609b9d)](https://www.codacy.com/manual/DDDdreamer/HappyThirteenWater-?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DDDdreamer/HappyThirteenWater-&amp;utm_campaign=Badge_Grade)
## 编译+运行环境
    无需编译！！！
    运行环境：windows + 工具版本：python3.7 + 运行前需先下载pyqt5、requests第三方库，可使用pip对pyqt5、requests库进行下载安装
 [pip使用教程](https://blog.csdn.net/m0_37774696/article/details/84328843)
## 食用方法
    AI算法分布在各个文件中，如需测试，打开httofunctions.py并运行即可；
    UI放在runn.py中，打开运行即可食用。
    可通过下载项目运行runn.py进行食用，食用过程中可能会出现页面卡顿的现象，还请各位耐心等待（无奈算法太low还跑得久），谢谢理解

    主要用法：
    打开.exe，进入登录界面，用已绑定的账号（没有的话点击注册进入注册界面进行注册）进行登录，登录成功后可进行
    开始游戏、排行榜（前四）、战局详情、历史对站查询等操作。
    开始游戏界面：点击“寻找战局”即可开始游戏，等待大概6-10s的时间即可自动出牌，再次点击可寻找新战局并自动出牌；
    排行榜：可查看排行榜前四名的排名；
    战局详情：输入战局id可查看该站距的玩家对战情况，包括得分和牌型；
    往期对战：输入page(页数)和user_id(用户名)即可查看自己的往期对战记录。
    注销：注销账号，返回登录界面
## 一些BUG
    1.开始游戏（包括寻找对局和出牌）：寻找战局之后会有6-7s的出牌时间，页面可能会卡顿；
    2.开启多个页面只能运行一个页面，比如同时开启寻找游戏和战局详情只能运行其中一个,否则会造成闪退；
    3.若UI开启时造成闪退，一般情况下由于服务器关闭引起的，只需等待服务器重新开启即可进入游戏;
    4.往期对战每页20条记录，对战局数不够的话无法显示；
    5.UI和AI都写得很丑，希望凑合着用QAQ！
