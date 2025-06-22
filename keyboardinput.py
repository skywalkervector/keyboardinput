from pynput import keyboard
import time

# 键盘控制状态
key_status = {
    'w': False,
    'a': False,
    's': False,
    'd': False,
    'j': False,
    'k': False
}

# 更新命令的函数
def update_commands():
    commands = {
        'forward': key_status['w'],
        'backward': key_status['s'],
        'left': key_status['a'],
        'right': key_status['d'],
        'left_rotation': key_status['j'],
        'right_rotation': key_status['k']
    }
    return commands

# 键盘事件处理
def on_press(key):
    try:
        if key.char in key_status:
            key_status[key.char] = True
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in key_status:
            key_status[key.char] = False
    except AttributeError:
        pass

# 启动键盘监听
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

def play(args):
    try:
        while True:
            commands = update_commands()
            print(f"Current commands: {commands}")
            time.sleep(0.1)  # 控制输出频率
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    play(args=None)