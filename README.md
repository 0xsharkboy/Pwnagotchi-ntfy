# ntfy plugin for pwnagotchi
A plugin that will send your pwnagotchi's main events to your devices through ntfy services.

<img src="https://github.com/0xsharkboy/Pwnagotchi-ntfy/assets/58356637/4148e13c-c42c-498b-9ed7-26acff8edb93" width="35%"/>

## Setup
1. Copy over `ntfy.py` into your custom plugins directory
2. In your `config.toml` file, add:
```toml
main.plugins.ntfy.enabled = true
main.plugins.ntfy.ntfy_url = "ntfy.sh/[ntfytopic]"
# Defines the priority of the notifications on your devices (see: https://docs.ntfy.sh/publish/#message-priority)
main.plugins.ntfy.priority = 3
# Should the plugin cache notifications as long as the pwnagotchi is offline ?
main.plugins.ntfy.cache_notifs = false
```
3. Restart your device and enjoy your ntfy plugin !

## Tracked events
 - Wake up
 - AI Ready
 - Deauth
 - Handshake capture
 - Association

## Recommandation
Since this plugin needs internet connection I higly recommend you to use [bt-tether](https://github.com/evilsocket/pwnagotchi/blob/master/pwnagotchi/plugins/default/bt-tether.py) plugin.

## To-do
 - [x] Notify on new peer/peer lost
 - [x] Save events until pwnagotchi is online
 - [ ] Notify session stats on shutdown