# TiebaSign
贴吧签到，模拟手机端进行百度贴吧批量签到的python3脚本。 2017
##更新

2017.2.18

增加发送邮件的功能

2017.2.11

全面使用Wap版贴吧，提高稳定性

2017.1.27

使用Wap版贴吧，提高速度且不需要验证码。

2017.1.26

注销百度账号时可能会销毁BDUSS

解决方案：不注销账号，直接删除浏览器的Cookie。

2017.1.25

发布 TiebaSign

##环境要求
1. python3
2. requests Lib

##使用说明
1.在**服务端**登陆你的百度账号(推荐用chrome+EditThisCookie插件)

2.打开网页 https://tieba.baidu.com/index.html

导出tieba.baidu.com的Cookies保存为user.json。

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
环境变量 export PYTHONIOENCODING="utf-8"

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

Login: 末日V4
Already signed in vb2010
Already signed in oblivious
Already signed in 尤里的复仇
Already signed in 红警3
```