
import logging
import logging.config
import os

"""
logging 四大组件：
    Logger:提供了应用程序可一直使用的接口
    Handler:将logger创建的日志记录发送到合适的目的输出
    Filter:提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
    Formatter:决定日志记录的最终输出格式  
"""

# log directory
log_dir = os.path.join(os.path.realpath(os.getcwd()), "logs")
print("log_dir:%s" % log_dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logging.config.dictConfig(
    {
        "version":1,
        "disable_existing_loggers": False,
        "formatters":{
            "format1":{
                "format":"%(asctime)s|%(threadName)s|%(name)s|%(levelname)-7s|%(filename)s:%(funcName)s:%(lineno)d|%(message)s"
            },
            "format2":{
                "format":"%(asctime)s %(threadName)s %(name)s %(levelname)-7s %(filename)s:%(funcName)s:%(lineno)d|%(message)s"
            }
        },
        "handlers":{
            "console":{
                "class":"logging.StreamHandler",
                "formatter":"format1",
                "level":"INFO",
                "stream":"ext://sys.stdout",
                "filters":["filter01"],
            },
            "console02":{
                "class":"logging.StreamHandler",
                "formatter":"format2",
                "level":"INFO",
                "stream":"ext://sys.stdout",
                "filters":["filter02"]
            },
            "all_log":{
                "class":"logging.handlers.RotatingFileHandler",
                "level":"INFO",
                "formatter":"format2",
                "filename": log_dir + "/all_info.log",
                "maxBytes": 10485760,
                "backupCount": 5,
                "encoding": "utf8"
            },
            "error_log":{
                "class":"logging.handlers.RotatingFileHandler",
                "level":"ERROR",
                "formatter":"format2",
                "filename": log_dir + "/error.log",
                "maxBytes": 10485760,
                "backupCount": 5,
                "encoding": "utf8"
            }
        },
        "filters":{
            "filter01":{
                "name":""
            },
            "filter02":{
                "name":"a.b.c"
            }
        },
        "loggers":{
            "a.b.c":{
                "level":  "INFO",
                "handlers": ["console"],
                "propagate": "no",
                "filters":["filter02"]
            }
        },
        "root":{
            "level": "INFO",
            "handlers":["console", "console02", "all_log", "error_log"]
        }
    }
)

if __name__ == "__main__":
    log = logging.getLogger("a")
    log.info("haha")
    log.error("abc")
