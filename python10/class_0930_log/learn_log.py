import logging


class MyLog:
    def my_log(self, level, msg):
        # 定义日志收集器
        my_logger = logging.getLogger('python10')   # 收集器名默认为root logger,此处为python10
        my_logger.setLevel('DEBUG')  # 设置收集级别

        # 定义输出渠道
        my_handler = logging.FileHandler('test_log.txt')    # StreamHandler()方法输出到控制台,FileHandler(filename)方法输出到文件
        my_handler.setLevel('DEBUG')  # 设置输出级别
        my_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(name)s - %(message)s"))

        # 绑定收集器和输出渠道
        my_logger.addHandler(my_handler)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 解绑渠道，否则日志会重复
        my_logger.removeHandler(my_handler)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug('debug message')
    my_logger.info('info message')
    my_logger.warning('warning message')
    my_logger.error('error message')
    my_logger.critical('critical message')
