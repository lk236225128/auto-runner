import os

if __name__ == '__main__':
    os.system(
        "python3 -m Fastbot_Android\\test -- adb -s J5AZB760T547H5K shell CLASSPATH=/sdcard/monkeyq.jar:/sdcard/framework.jar exec app_process /system/bin com.android.commands.monkey.Monkey -p com.baidu.app --agent robot --running-minutes 2 --throttle 500 -v -v")


