#!/usr/bin/env python

import os

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

notify(
    title    = 'A Real Notification',
    subtitle = 'with python',
    message  = 'Hello, this is me, notifying you!'
)