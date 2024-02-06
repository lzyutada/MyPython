'''
publish web files to specified directory.
each publish action will be logged into DB table(publish list).
each published file will be logged into DB table(publish file list) assosiated with publish action.
about publish list:
+-------+--------------+------------+---------------+-----------+-----------+-----------+-----------+-------+-----------+-----------+
| PublishId | FileCount | PublishStatus |    AddTime   | AddDate   | LastTime  | LastDate  | IsDel | Remark    | Disorder  |
+-------+--------------+------------+---------------+-----------+-----------+-----------+-----------+-------+-----------+-----------+
|   2   |   15  | 1(SUCCESS)  | 2023-12-21 15:02:49 | 2023-12-21 | 2023-12-21 15:02:49 | 2023-12-21 | 0 | This is a remark |   0 |

about published file list:
+-------+--------------+------------+---------------+-----------+-----------+-----------+-----------+-------+-----------+-----------+
| PublishFileId | PublishId | PublishStatus     | FilePath   |  Md5   | AddTime   | AddDate   | LastTime  | LastDate  | IsDel | Remark    | Disorder  |
+-------+--------------+------------+---------------+-----------+-----------+-----------+-----------+-------+-----------+-----------+
|   14          |   2       | 1(SUCCESS)        | Y:\\TFS\\FromTFS2015\\MisNet2014\\MisNet2014\\bin\\a1017_Redis.dll    |  md5des |   2023-12-21 15:02:49 | 2023-12-21 | 2023-12-21 15:02:49 | 2023-12-21 | 0 | This is a test document |   0 |
''' 

import os
import hashlib
import shutil
import traceback
import mysql.connector
import datetime
from datetime import datetime
import dbhelper.mysql.pymysqlhelper
from loghelper.loghelper import get_logger
from constances.constances import PublishStatus, PublishLogList, PublishFileList
from logging.handlers import TimedRotatingFileHandler

def __get_file_count(folder): 
    file_count = 0
    for _, _, files in os.walk(folder):
        file_count += len(files)
    return file_count

def __create_target_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def __get_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def __insert_publish_record(mydb, mycursor, total_files_count, success_files_count, publish_status):
    '''
    add publish log item
    :param total_files_count: for [@TABLENAME_PUBLOG].[PubFileCount]
    :param success_files_count: for [@TABLENAME_PUBLOG].[PubSuccessFileCount]
    :param publish_status: for [@TABLENAME_PUBLOG].[PublishStatus]
    :returns: return [@TABLENAME_PUBLOG].[PublishId] of the new added row.
    :rtype: integer
    '''
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_date = datetime.now().strftime("%Y-%m-%d")

    # 在数据库中插入发布记录
    sql = F"INSERT INTO {PublishLogList.TABLENAME_PUBLOG} ( \
        {PublishLogList.COLNAME_PUBLOG_PUBFILECOUNT}, \
        {PublishLogList.COLNAME_PUBLOG_PUBSUCCESSFILECOUNT}, \
        {PublishLogList.COLNAME_PUBLOG_PUBLISHSTATUS}, \
        {PublishLogList.COLNAME_PUBLOG_ADDTIME}, \
        {PublishLogList.COLNAME_PUBLOG_ADDDATE}, \
        {PublishLogList.COLNAME_PUBLOG_LASTTIME}, \
        {PublishLogList.COLNAME_PUBLOG_LASTDATE} \
        ) VALUES ( \
        '{total_files_count}', \
        '{success_files_count}', \
        '{publish_status}', \
        '{add_time}', \
        '{add_date}', \
        '{add_time}', \
        '{add_date}')"
    mycursor.execute(sql)
    mydb.commit()
    return mycursor.lastrowid

def __insert_publish_file_detail(mydb, mycursor, publish_id, file_path, md5):
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_date = datetime.now().strftime("%Y-%m-%d")
    # 在数据库中插入发布文件明细
    sql = F"INSERT INTO {PublishFileList.TABLENAME_PUBFILELIST} ( \
        {PublishFileList.COLNAME_PUBFILE_PUBLISHID}, \
        {PublishFileList.COLNAME_PUBFILE_FILEPATH}, \
        {PublishFileList.COLNAME_PUBFILE_FILEMD5}, \
        {PublishFileList.COLNAME_PUBFILE_ADDTIME}, \
        {PublishFileList.COLNAME_PUBFILE_ADDDATE}, \
        {PublishFileList.COLNAME_PUBFILE_LASTTIME}, \
        {PublishFileList.COLNAME_PUBFILE_LASTDATE} \
        ) VALUES ( \
        '{publish_id}', \
        '{file_path}', \
        '{md5}', \
        '{add_time}', \
        '{add_date}', \
        '{add_time}', \
        '{add_date}')"
    mycursor.execute(sql)
    mydb.commit()

def copy_files(src, des):
    logger = get_logger()
    
    DB_CONN_INFO = dbhelper.mysql.pymysqlhelper.getConnectInfo()

    # 连接数据库
    mydb = mysql.connector.connect(
        host = DB_CONN_INFO.host,
        user = DB_CONN_INFO.username,
        password = DB_CONN_INFO.password,
        database = DB_CONN_INFO.dbname,
        charset = 'utf8' # 设置字符集
    )
    mycursor = mydb.cursor()

    __create_target_folder(des)  # makesure des folder exist
    logger.debug("create target folder complete")

    totalFileCount = __get_file_count(src)    #
    logger.debug(F"total file count: {totalFileCount}")

    publish_id = __insert_publish_record(mydb, mycursor, totalFileCount, 0, PublishStatus.PUBSTATUS_PUBLISHING) #
    logger.debug(F"new publis log id: {publish_id}")

    pubIgnoreCount = 0
    success_files_count = 0
    for foldername, subfolders, filenames in os.walk(src):
        for filename in filenames:
            file_path = os.path.join(foldername, filename).replace('\\', '\\\\')
            relative_path = os.path.relpath(file_path, src)
            target_file_path = os.path.join(des, relative_path)
            # logger.debug(F"filename: {file_path}")

            dbgmsg = "File: %s\n\t" % (file_path, )

            # 判断文件类型和.vs文件夹
            if not filename.endswith((".csproj", ".csproj.")) \
                and ".vs" not in file_path \
                and os.path.join("writedir", "logs").replace('\\', '\\\\') not in file_path :
                md5 = __get_md5(file_path)
                dbgmsg = dbgmsg + "---file MD5: %s\n\t" % (md5, )

                target_directory = os.path.dirname(target_file_path)
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)

                # 查询数据库中最新的MD5值
                sql = F"SELECT \
                            {PublishFileList.COLNAME_PUBFILE_FILEMD5} \
                        FROM {PublishFileList.TABLENAME_PUBFILELIST} \
                        WHERE \
                            {PublishFileList.COLNAME_PUBFILE_FILEPATH} = '{file_path}' \
                        ORDER BY {PublishFileList.COLNAME_PUBFILE_PUBLISHFILEID} DESC \
                        LIMIT 1"
                mycursor.execute(sql)
                result = mycursor.fetchone()
                if result and result[0] == md5:
                    dbgmsg = dbgmsg + F"---file ignored: the same MD5({result[0]})\n\t"
                    pubIgnoreCount = pubIgnoreCount + 1 # 文件没有改动，不拷贝
                else:
                    # 文件有改动，拷贝并更新数据库
                    shutil.copy2(file_path, target_file_path)
                    __insert_publish_file_detail(mydb, mycursor, publish_id, file_path, md5)
                    success_files_count += 1
                    dbgmsg = dbgmsg + F"---({success_files_count}th)file copied to: {target_file_path}\n\t"
            else:
                dbgmsg = dbgmsg + "---file ignored.\n\t"
                pubIgnoreCount = pubIgnoreCount + 1 # ignored file or path
            
            logger.debug(dbgmsg)

    if totalFileCount == (success_files_count + pubIgnoreCount):
        publish_status = PublishStatus.PUBSTATUS_SUCCESS  # 如果所有文件都成功拷贝，则更新为成功状态
    else : 
        publish_status = PublishStatus.PUBSTATUS_FAILED

    # 更新发布记录中的状态和成功文件数量
    upd_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    upd_date = datetime.now().strftime("%Y-%m-%d")
    sql = F"UPDATE {PublishLogList.TABLENAME_PUBLOG} \
        SET {PublishLogList.COLNAME_PUBLOG_PUBSUCCESSFILECOUNT} = '{success_files_count}', \
        {PublishLogList.COLNAME_PUBLOG_PUBIGNOREFILECOUNT} = '{pubIgnoreCount}', \
        {PublishLogList.COLNAME_PUBLOG_PUBLISHSTATUS} = '{publish_status}', \
        {PublishLogList.COLNAME_PUBLOG_LASTTIME} = '{upd_time}', \
        {PublishLogList.COLNAME_PUBLOG_LASTDATE} = '{upd_date}' \
         WHERE \
            {PublishLogList.COLNAME_PUBLOG_PUBLISHID} = '{publish_id}'\
        "
    mycursor.execute(sql)
    mydb.commit()

    logger.debug(F"update publish record finished")
