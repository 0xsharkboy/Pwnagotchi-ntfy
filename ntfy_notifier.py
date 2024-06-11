import logging

import pwnagotchi.plugins as plugins

class NtfyNotifier(plugins.Plugin):
    __author__ = '0xSharkboy'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin that sends notifications to your ntfy client'

    def __init__(self):
        self.options = dict()
        self.url = None

    def on_loaded(self):
        self.url = f'https://{self.options["ntfy_url"]}'

        if self.options["ntfy_url"]:
            logging.info(f"[Ntfy Notifier]: plugin loaded with the url: {self.url}")
        else:
            logging.warning("[Ntfy Notifier]: No URL specified! Plugin will not send notifications.")
