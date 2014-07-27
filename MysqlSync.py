#coding=utf8

import MySQLdb
import datetime
import time
import traceback


# 再此处设置数据库
HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASSWD = "root"
DB = "test"


while True:
    # 获取开始时间
    stime = time.time()
    try:
        # 获取当前日期字符串和1分钟前日期字符串
        now = datetime.datetime.now()
        prev = now - datetime.timedelta(minutes=1)
        now = now.strftime("%Y-%m-%d %H:%M:00")
        prev = prev.strftime("%Y-%m-%d %H:%M:00")
        print "-----------", now, "-----------"

        # 创建MySQL连接 已经一个游标
        conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)
        cur = conn.cursor()

        # 查询语句
        sql = """
        select CMID, SkillNum, MonitorTime, WithSLPercent, ACDAgents, ACWAgents, StaffedAgents, WaitingCalls  
        from `pbx_MonitorBCMSSkill` 
        where ( SkillNum='1201' or SkillNum='1202' ) 
        and CreateTime BETWEEN '%s' and  '%s'
        """ % (prev, now)
        # 执行语句
        cur.execute(sql)

        # 查询结果
        rs = cur.fetchall()
        # 逐个处理查询结果
        for r in rs:
            print r
            CMID = r[0]
            SkillNum = r[1]
            MonitorTime = r[2]
            WithSLPercent = r[3]
            ACDAgents = int(r[4])
            ACWAgents = int(r[5])
            StaffedAgents = int(r[6])
            WaitingCalls = int(r[7])

            # 计算得到新表变量
            SkillLevel = WithSLPercent
            HOLD_AGENT = 1.0 * (ACDAgents + ACWAgents) / StaffedAgents
            QUEUE_AGENT = 1.0 * WaitingCalls / StaffedAgents

            # 插入新表语句
            sql = """
            insert into `Traffic distribution`(`CMID`, `SkillNum`, `MonitorTime`, `SkillLevel`, `HOLD/AGENT`, `QUEUE/AGENT`, `VDN/AGENT`, `ABAND/AGENT`, `AVGANS`, `AVGABAND`) 
            values(%s, %s, '%s', %s, %s, %s, 0, 0, 0, '')
            """ % (CMID, SkillNum, MonitorTime, SkillLevel, HOLD_AGENT, QUEUE_AGENT)
            # 执行语句
            cur.execute(sql)

            print "Sync:", CMID

        # 提交事务 并关闭连接
        conn.commit()
        cur.close()
        conn.close()

    except:
        traceback.print_exc()

    # 获取结束时间 这样就能得到这一次同步所用的时间，然后延时60秒
    etime = time.time()
    dtime = etime - stime
    time.sleep(60 - dtime)