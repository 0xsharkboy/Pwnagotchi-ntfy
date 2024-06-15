import logging
import requests

import pwnagotchi.plugins as plugins

'''
Here's an example configuration for this plugin:
main.plugins.ntfy.enabled = true
main.plugins.ntfy.ntfy_url = "ntfy.sh/[ntfylink]"
# Defines the priority of the notifications on your devices (see: https://docs.ntfy.sh/publish/#message-priority)
main.plugins.ntfy.priority = 3
'''

class ntfy(plugins.Plugin):
    __author__ = '0xsharkboy'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin that sends notifications to your devices through ntfy services.'

    def __init__(self):
        self.options = dict()
        self.url = None
        self.priority = None
        self.name = None

    def _check_options(self):
        if 'ntfy_url' not in self.options:
            self.options["ntfy_url"] = ""
        if 'priority' not in self.options or not (1 <= self.options["priority"] <= 5):
            self.options["priority"] = 3

    def on_loaded(self):
        self._check_options()
        self.priority = self.options["priority"]

        if self.options["ntfy_url"]:
            self.url = f'https://{self.options["ntfy_url"]}'
            logging.info(f'[ntfy] plugin loaded with the url: {self.options["ntfy_url"]}')
        else:
            logging.warning('[ntfy] plugin loaded but no URL specified! Plugin will not send notifications.')

    def _send_notification(self, title, message):
        if not self.url:
            return

        try:
            requests.post(
                self.url,
                headers={
                    'Title': title,
                    'Priority' : str(self.priority)
                },
                data=message
            )
        except requests.RequestException as e:
            logging.warning(f'[ntfy] notification not sent due to: {e}')

    def on_ready(self, agent):
        if not self.name:
            self.name = agent._config["main"]["name"]

        self._send_notification(f'{self.name} woke up', 'Let\'s pwn the world!')
    
    def on_ai_ready(self, agent):
        self._send_notification('AI is ready', 'Let\'s learn together!')

    def on_association(self, agent, access_point):
        ssid = access_point.get("hostname", '')
        bssid = access_point.get("mac", '')
        what = ssid if ssid != '' and ssid != '<hidden>' else bssid

        self._send_notification('Hey!', f'{self.name} is associating to {what}')

    def on_peer_detected(self, agent, peer):
        self._send_notification('Peer Detected!', f'{self.name} detected a new peer: {peer}')

    def on_peer_lost(self, agent, peer):
        self._send_notification('Peer Lost', f'{self.name} lost contact with peer: {peer}')

    def on_deauthentication(self, agent, access_point, client_station):
        client = client_station.get("hostname", client_station["mac"])
        access = access_point.get("hostname", access_point["mac"])

        self._send_notification('Deauth!', f'{self.name} is deauthenticating {client} from {access}')

    def on_handshake(self, agent, filename, access_point, client_station):
        access = access_point.get("hostname", access_point["mac"])

        self._send_notification('Pwned!', f'{self.name} has captured a new handshake from {access}')