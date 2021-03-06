#!/usr/bin/env python3
# License: GPL-3.0
# Description: starts the both client and admin HTTPS servers

from sys import exit
from threading import Thread
from server.db import init_db
from server.ClientServer.server import ClientServer
from server.AdminServer.server import AdminServer

try:
    # TransportC2 v0.08
    init_db()
    Thread(target=ClientServer).start()
    Thread(target=AdminServer).start()
except KeyboardInterrupt:
    exit(0)
