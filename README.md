# TiebaSign
贴吧签到，模拟手机端进行百度贴吧批量签到的python3脚本。 2019年更新


## 环境要求
1. python3
2. requests Lib  

Win10 + Ubuntu 18.04 测试通过
## 使用说明
1. 在**服务端**登陆你的百度账号
2. 打开网页 https://tieba.baidu.com/index.html
3. 保存Cookie(两种方法)  
    
    方法1： Chrome或Firefox浏览器抓包 保存为txt文件  
    格式如下：
    ```
    BAIDUID=74D6**; BIDUPSID=7**; PSTM=15**; BDUSS=**; ****
    ```
    方法2： Chrome + EditThisCookie插件 保存为json文件  
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

4. 把user.json或user.txt放入Tieba文件夹
5. 运行 run.py

> 默认签到延时10秒钟，在run.py中可以修改delay参数

> Linux下可能需要环境变量 export PYTHONIOENCODING="utf-8"  
## 部署
```bash
jzc@ubuntu:~$ wget https://github.com/jiangzc/TiebaSign/archive/master.zip
jzc@ubuntu:~$ unzip master.zip
jzc@ubuntu:~$ mv TiebaSign-master/ TiebaSign/
jzc@ubuntu:~$ cd TiebaSign/
# add user's json or txt file
jzc@ubuntu:~/TiebaSign$ export PYTHONIOENCODING="utf-8"
jzc@ubuntu:~/TiebaSign$ python3 run.py
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

## 更新记录
2019.3.5  
重构项目，更新README  
2017.7.31  
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