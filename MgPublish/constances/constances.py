class PublishStatus :
    PUBSTATUS_UNKNOWN           = 0
    PUBSTATUS_SUCCESS           = 1
    PUBSTATUS_PARTIALSUCCESS    = 2
    PUBSTATUS_FAILED            = 3
    PUBSTATUS_PUBLISHING        = 4

class PublishLogList :
    '''
    definition for table 'PublishLogList'
    '''
    TABLENAME_PUBLOG                        = "PublishLogList"
    COLNAME_PUBLOG_PUBLISHID                = "PublishId"
    COLNAME_PUBLOG_PUBFILECOUNT             = "PubFileCount"
    COLNAME_PUBLOG_PUBSUCCESSFILECOUNT      = "PubSuccessFileCount"
    COLNAME_PUBLOG_PUBLISHSTATUS            = "PublishStatus"
    COLNAME_PUBLOG_ADDTIME                  = "AddTime"
    COLNAME_PUBLOG_ADDDATE                  = "AddDate"
    COLNAME_PUBLOG_LASTTIME                 = "LastTime"
    COLNAME_PUBLOG_LASTDATE                 = "LastDate"
    COLNAME_PUBLOG_ISDEL                    = "IsDel"
    COLNAME_PUBLOG_REMARK                   = "Remark"
    COLNAME_PUBLOG_DISORDER                 = "Disorder"
    COLNAME_PUBLOG_PUBIGNOREFILECOUNT       = "PubIgnoreFileCount"

class PublishFileList :
    '''
    definition for table 'PublishFileList'
    '''
    TABLENAME_PUBFILELIST           = "PublishFileList"
    COLNAME_PUBFILE_PUBLISHFILEID	=	"PublishFileId"
    COLNAME_PUBFILE_PUBLISHID	    =	"PublishId"
    COLNAME_PUBFILE_PUBLISHSTATUS	=	"PublishStatus"
    COLNAME_PUBFILE_FILEPATH	    =	"FilePath"
    COLNAME_PUBFILE_FILEMD5     	=	"FileMd5"
    COLNAME_PUBFILE_ADDTIME	        =	"AddTime"
    COLNAME_PUBFILE_ADDDATE     	=	"AddDate"
    COLNAME_PUBFILE_LASTTIME	    =	"LastTime"
    COLNAME_PUBFILE_LASTDATE	    =	"LastDate"
    COLNAME_PUBFILE_ISDEL       	=	"IsDel"
    COLNAME_PUBFILE_REMARK	        =	"Remark"
    COLNAME_PUBFILE_DISORDER	    =	"Disorder"

