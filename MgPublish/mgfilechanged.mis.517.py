# # '''
# # '''

# import os
# import time
# import traceback
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from watchdog.observers.polling import PollingObserver
# import logging
# from logging.handlers import TimedRotatingFileHandler
# import datetime
# from datetime import datetime

# SOURCE_FOLDER = r"Y:\TFS\TPC_Website\tp_website_mis2020\website_mis2020"
# # SOURCE_FOLDER = r"C:\inetpub\wwwroot\mis.517.my"

# # 获取当前日期
# current_date = datetime.now().strftime('%Y%m%d')
# log_folder = 'log'

# # 如果log文件夹不存在，则创建
# if not os.path.exists(log_folder):
#     os.makedirs(log_folder)
# log_file = os.path.join(log_folder, f'{current_date}.log')

# # 创建日志记录器
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # 创建 TimedRotatingFileHandler
# file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=0)
# file_handler.setLevel(logging.DEBUG)

# # 创建日志格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# # 添加处理器到日志记录器
# logger.addHandler(file_handler)

# class RecursiveHandler(FileSystemEventHandler):
#     # def on_any_event(self, event) :
#     #     print("event[%s] happend" % (event.event_type))

#     def on_modified(self, event):
#         # print("on modified")
#         if event.is_directory:
#             return
#         logger.debug(f'File {event.src_path} has been modified')

#     def on_created(self, event):
#         # print("on created")
#         if event.is_directory:
#             return
#         logger.debug(f'File {event.src_path} has been created')

# if __name__ == "__main__":
#     folder_to_watch = SOURCE_FOLDER
#     event_handler = RecursiveHandler()
#     observer = PollingObserver() # Observer()
#     observer.schedule(event_handler, folder_to_watch, recursive=True)
#     logger.debug("start observer")
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         logger.debug("stop observer by user canceled.")
#         observer.stop()
#     except BaseException as err:
#         logger.debug("observer error: %s\r\n调用堆栈: %s" % (str(err), traceback.format_exc()))
#     observer.join()
    
# # import time
# # from watchdog.observers.polling import PollingObserver
# # # from watchdog.observers import PollingObserver
# # from watchdog.events import FileSystemEventHandler

# # SOURCE_FOLDER = r"Y:\TFS\FromTFS2015\MisNet2014\MisNet2014"

# # class MyHandler(FileSystemEventHandler):
# #     def on_modified(self, event):
# #         if event.is_directory:
# #             return
# #         print(f"File {event.src_path} has been modified")

# # if __name__ == "__main__":
# #     folder_to_watch = SOURCE_FOLDER  # Replace with your shared folder path
# #     event_handler = MyHandler()
# #     observer = PollingObserver(1)  # Polling every 1 second
    
# #     observer.schedule(event_handler, folder_to_watch, recursive = True)
# #     observer.start()
    
# #     try:
# #         while True:
# #             time.sleep(1)
# #     except KeyboardInterrupt:
# #         observer.stop()
# #         observer.join()