import sys
import platform


def flags_count_for_ping_depending_os():
    if platform.system().lower() == 'windows':
        return '-n'
    else:
        return '-c'


def is_exist_pathname(pathname):
    try:
        with open(pathname) as f:
            # remove '\n' if it's at the end of the line
            return [line[:-1] if line[-1] == '\n' else line for line in f]
    except FileNotFoundError:
        sys.exit('File not found')
    except:
        sys.exit('Error while reading file')
