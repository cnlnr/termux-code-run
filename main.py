from watchfiles import watch, Change
import os
import time

watch_path = '/storage/emulated/obb/实验/'
try:
    for changes in watch(watch_path):
        for change_type, file_path in changes:
            if change_type == Change.modified and file_path.endswith('.py'):
                os.system("clear")
                os.system("am start -n com.termux/.app.TermuxActivity > /dev/null 2>&1")
                start = time.time()
                exit_code = \
os.system(f"python {file_path}")
                end = time.time()
                input(f"[退出代码 {exit_code}, 用时 {end - start :.2f} 秒]")
                os.system("am start -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n bin.mt.plus/.Main > /dev/null 2>&1")
except KeyboardInterrupt:
    exit()