def get_logger():
    '''
    '''

    import os
    import datetime
    from datetime import datetime
    import logging
    from logging.handlers import TimedRotatingFileHandler
        
    # 获取当前日期
    current_date = datetime.now().strftime('%Y%m%d')
    log_folder = 'log'

    # 如果log文件夹不存在，则创建
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, f'{current_date}.log')

    # 创建日志记录器
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 创建 TimedRotatingFileHandler
    file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=0)
    file_handler.setLevel(logging.DEBUG)

    # 创建日志格式
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s')
    file_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    return logger
