import logging
import requests

import pwnagotchi.plugins as plugins

class ntfy(plugins.Plugin):
    __author__ = '0xSharkboy'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin that sends notifications to your ntfy client'

    def __init__(self):
        self.options = dict()
        self.url = None

    def on_loaded(self):
        if 'ntfy_url' not in self.options:
            self.options["ntfy_url"] = ""

        if self.options["ntfy_url"]:
            self.url = f'https://{self.options["ntfy_url"]}'
            logging.info(f'[ntfy] plugin loaded with the url: {self.options["ntfy_url"]}')
        else:
            self.url = None
            logging.warning('[ntfy] plugin loaded but no URL specified! Plugin will not send notifications.')

    def _send_notification(self, title, message):
        if not self.url:
            return

        try:
            requests.post(
                self.url,
                headers={
                    'Title': title
                },
                data=message
            )
        except:
            logging.warning('[ntfy] Notification not sent.')
            pass

    def on_ready(self, agent):
        self._send_notification('Pwnagotchi Ready', 'Your pwnagotchi is ready to pwn!')

    def on_sleep(self, agent, t):
        self._send_notification('Pwnagotchi Sleeping', f'Your pwnagotchi is going to sleep for {t} seconds.')
    
    def on_ai_ready(self, agent):
        self._send_notification('AI Ready', f'Your pwnagotchi AI mode is ready!')
