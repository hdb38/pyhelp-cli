from .level import Level, INFO, SUCCESS, WARN, ERROR
from typing import Optional

class Log(object):
    @classmethod
    def switch_level(cls, level: Optional[Level]):
        if not isinstance(level, Level):
                raise RuntimeError("日志级别必须是 Level 类型")
        if isinstance(level, INFO):
            return "INFO"
        elif isinstance(level, SUCCESS):
            return "SUCCESS"
        elif isinstance(level, WARN):
            return "WARN"
        elif isinstance(level, ERROR):
            return "ERROR"
        return "UNKNOWN"

    @classmethod
    def get_nowtime(cls):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def get_string(cls, level: Level, message: str):
        return f"[{Log.get_nowtime()}] {Log.switch_level(level)} {message}"

    @classmethod
    def write_to_file(cls, level: Level, message: str):
        log_path = __file__.replace("log.py", "log.log")
        with open(log_path, "a", encoding="utf-8") as fp:
            fp.write(Log.get_string(level, message) + "\n")
    
    @classmethod
    def clean_file(cls):
        log_path = __file__.replace("log.py", "log.log")
        with open(log_path, "w", encoding="utf-8") as fp:
            fp.write("--- BEGIN Log ---\n")
