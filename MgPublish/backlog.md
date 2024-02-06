# Create table of 'PublishLogList'
```
CREATE TABLE IF NOT EXISTS PublishLogList (
    PublishId INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '(PK)publish log id',
    PubFileCount INT NOT NULL DEFAULT '0' COMMENT 'total file count for this publish',
    PubSuccessFileCount INT NOT NULL DEFAULT '0' COMMENT 'file count of publish successfully',
    PublishStatus INT NOT NULL DEFAULT '0' COMMENT 'publish status, 0 - unknown; 1 - success; 2 - partial success; 3 - common failure',
	AddTime DATETIME NOT NULL COMMENT 'add time',
	AddDate DATE NOT NULL COMMENT 'add date',
	LastTime DATETIME NOT NULL COMMENT 'latest update time',
	LastDate DATE NOT NULL COMMENT 'latest updated date',
	IsDel INT NOT NULL DEFAULT '0' COMMENT 'deleted status',
	Remark VARCHAR ( 4000 ) NOT NULL DEFAULT '' COMMENT 'remark',
    Disorder INT NOT NULL DEFAULT '0' COMMENT 'disorder' 
)
```



# Create table of 'PublishFileList'
```
CREATE TABLE IF NOT EXISTS PublishFileList (
	PublishFileId INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '(PK)publish file id',
	PublishId INT NOT NULL DEFAULT '0' COMMENT '(FK)publish log id',
	PublishStatus INT NOT NULL DEFAULT '0' COMMENT 'publish status, 0 - unknown; 1 - success; 2 - partial success; 3 - common failure',
	FilePath VARCHAR ( 4000 ) NOT NULL DEFAULT '' COMMENT 'fullpath of file',
	FileMd5 VARCHAR ( 4000 ) NOT NULL DEFAULT '' COMMENT 'md5 of file',
	AddTime DATETIME NOT NULL COMMENT 'add time',
	AddDate DATE NOT NULL COMMENT 'add date',
	LastTime DATETIME NOT NULL COMMENT 'latest update time',
	LastDate DATE NOT NULL COMMENT 'latest updated date',
	IsDel INT NOT NULL DEFAULT '0' COMMENT 'deleted status',
	Remark VARCHAR ( 4000 ) NOT NULL DEFAULT '' COMMENT 'remark',
	Disorder INT NOT NULL DEFAULT '0' COMMENT 'disorder' 
)
```
