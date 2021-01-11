"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
from tool import log as _log
from itertools import count
import time
from parser import get_projects

log = _log("MAIN", "main.log")
log.info("This logger for main script")

WAITH = 60 * 2

def work():
    projects = get_projects()
    log.info("%s" % projects)

def main():
    for _ in count():
        try:
            work()
            log.info("Count: %s" % _)
            time.sleep(WAITH)
        except Exception as e:
            log.error("Error %s" % e, exc_info=True)
            time.sleep(60 * 1)


if __name__ == '__main__':
    main()