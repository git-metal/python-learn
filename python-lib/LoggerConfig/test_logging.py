
import os
import logging

# log directory
log_dir = os.path.join(os.path.realpath(os.getcwd()), "logs")
print("log_dir:%s" % log_dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# 默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
logging.basicConfig(level=logging.INFO,
                    filename=log_dir + "/test.log",
                    format="%(asctime)s|%(threadName)s|%(name)s|%(levelname)-7s|%(filename)s:%(funcName)s:%(lineno)d|%(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S %a'
                    )

def test_func():
    logging.info("test func")

logging.debug("debug msg")
logging.info("info msg")
logging.warning("waring msg")
logging.error("error msg")
logging.critical("critical msg")
test_func()
logging.info("name:%s year:%d" %("china", 2018))

log = logging.getLogger("mylogger")
log.info("hello world!")
