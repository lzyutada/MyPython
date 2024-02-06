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

def __publish_all():
    from publishhelper.publishhelper import copy_files
    SOURCE_FOLDER = r"Y:\TFS\TPC_Website\tp_webapi_mis2020\webapi_mis2020"
    TARGET_FOLDER = r"C:\inetpub\wwwroot\misapi2020.517api.my"
    copy_files(SOURCE_FOLDER, TARGET_FOLDER)

try : 
    import sys
    import traceback

    __publish_all()
    # argument = sys.argv[1:2][0]
    
    #
#     PUB_DICT = {
#         "a10" : __publish_a10,
#         "517bc" : __publish_517bc,
#     }

#     try :
#         func = PUB_DICT[argument]
#         func()
#     except KeyError:
#         print("unsupported module: %s" % (argument,))

# except IndexError:
#     __publish_all()
except BaseException as err:
    print("publish error: %s\r\nstacktrace: %s" % (str(err), traceback.format_exc()))
