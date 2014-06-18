#coding=utf8

import MySQLdb
import datetime
import time
import traceback

HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASSWD = "root"
DB = "test"


while True:
    try:
        now = datetime.datetime.now()
        prev = now - datetime.timedelta(minutes=1)
        now = now.strftime("%Y-%m-%d %H:%M:00")
        prev = prev.strftime("%Y-%m-%d %H:%M:00")
        print "-----------", now, "-----------"

        conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB)
        cur = conn.cursor()

        sql = """
        select CMID, SkillNum, MonitorTime, WithSLPercent, ACDAgents, ACWAgents, StaffedAgents, WaitingCalls  
        from `pbx_MonitorBCMSSkill` 
        where ( SkillNum='1201' or SkillNum='1202' ) 
        and CreateTime BETWEEN '%s' and  '%s'
        """ % (prev, now)
        cur.execute(sql)

        rs = cur.fetchall()

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

            SkillLevel = WithSLPercent
            HOLD_AGENT = 1.0 * (ACDAgents + ACWAgents) / StaffedAgents
            QUEUE_AGENT = 1.0 * WaitingCalls / StaffedAgents

            sql = """
            insert into `Traffic distribution`(`CMID`, `SkillNum`, `MonitorTime`, `SkillLevel`, `HOLD/AGENT`, `QUEUE/AGENT`, `VDN/AGENT`, `ABAND/AGENT`, `AVGANS`, `AVGABAND`) 
            values(%s, %s, '%s', %s, %s, %s, 0, 0, 0, '')
            """ % (CMID, SkillNum, MonitorTime, SkillLevel, HOLD_AGENT, QUEUE_AGENT)
            cur.execute(sql)

            print "Sync:", CMID

        conn.commit()
        cur.close()
        conn.close()

    except:
        traceback.print_exc()

    time.sleep(50)