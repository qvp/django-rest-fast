import os
from urllib.parse import urljoin

from django.conf import settings
from decouple import config


def open_browser(uri: str = '/'):
    """Запускает окно браузера с нужным URL."""
    command = '"{chrome_path}" --app={url} --window-size={window_size} --no-referrers --incognito --disable-plugins'
    os.system(command.format(**{
        'chrome_path': config('BROWSER_EXE_PATH'),
        'url': urljoin(settings.APP_URL, uri),
        'window_size': config('CHROME_WINDOW_SIZE'),
    }))


def browser_focus():
    """Делает окно браузера в фокусе."""
    cmd = rf'call {settings.BASE_DIR}\scripts\utils\sendkeys.bat "{settings.APP_NAME}" ""'
    os.system(cmd)
