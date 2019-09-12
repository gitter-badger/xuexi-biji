#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("无法导入Django!\
            您确定它已经安装在您的PYTHONPATH环境变量上并且可用吗？\
            你忘记激活虚拟环境了吗？") from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
