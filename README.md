# TiebaSign
贴吧签到，模拟手机端进行百度贴吧批量签到的python3脚本。 2017
## 更新
2017.7.15

更新文档

2017.5.27

修复master分支的BUG

2017.4.9

优化代码

2017.2.11

全面使用Wap版贴吧，提高稳定性

2017.1.27

使用Wap版贴吧，提高速度且不需要验证码。

2017.1.26

注销百度账号时可能会销毁BDUSS

解决方案：不注销账号，直接删除浏览器的Cookie。

2017.1.25

发布 TiebaSign

## 环境要求
1. python3
2. requests Lib

## 使用说明
1.在**服务端**登陆你的百度账号(推荐用chrome+EditThisCookie插件)

2.打开网页 https://tieba.baidu.com/index.html

导出tieba.baidu.com的Cookies保存为user.json。

格式如下：有效参数name, value
```
  [
  {
    "**": "***",
    "name": "BAIDUID",
    "value": "8075270406317538E68D2*****:FG=1",
  },

  {
    "**": "***",
    "name": "BDUSS",
    "value": "XVSUlM2N29oWn***Q",
  },
  .......
 ]
```

3.把user.json放入Tieba文件夹

4.运行main.py
环境变量 export PYTHONIOENCODING="utf-8"

## 部署
```bash
jzc@ubuntu:~$ wget https://github.com/jiangzc/TiebaSign/archive/master.zip
jzc@ubuntu:~$ unzip master.zip
jzc@ubuntu:~$ mv TiebaSign-master/ TiebaSign/
jzc@ubuntu:~$ cd TiebaSign/
jzc@ubuntu:~/TiebaSign$ chmod +x main.py
# add user's json file
jzc@ubuntu:~/TiebaSign$ export PYTHONIOENCODING="utf-8"
jzc@ubuntu:~/TiebaSign$ ./main.py
```

## 输出样本
```
Local Time: Sat May 27 18:30:44 2017
Login: 末日V4
['vb2010', 'oblivious', '尤里的复仇', '红警3', 'python3']
末日V4 Signing
Already signed in vb2010
Already signed in oblivious
Already signed in 尤里的复仇
Already signed in 红警3
```