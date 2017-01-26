# TiebaSign
模拟PC端进行百度贴吧批量签到的python3脚本 2017
##更新时间
2017.1.25

##环境要求
1. python3
2. requests Lib

##使用说明
1.在**服务端**登陆你的百度账号(推荐用chrome+EditThisCookie插件)

2.导出tieba.baidu.com的Cookies保存为user.json。
  格式如下：有效参数name, value
```
  [
  {
    "name": "BAIDUID",
    "value": "8075270406317538E68D2*****:FG=1",
  },

  {
    "name": "BDUSS",
    "value": "XVSUlM2N29oWn***Q",
  },
  .......
 ]
```

3.把user.json放入Tieba文件夹

4.运行main.py

##输出样本
```
jzc@125295:~$ export PYTHONIOENCODING="utf-8"
jzc@125295:~$ echo $PYTHONIOENCODING
utf-8
jzc@125295:~$ python3 /home/jzc/Tieba/main.py
```
```
Login: 53y7fhy
Already signed in 鬼
Already signed in oblivious
```