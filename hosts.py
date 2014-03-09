#!/usr/bin/env python

import argh
from chef import Node, autoconfigure

def hosts(env=None):
    api = autoconfigure()
    nodes = (node for node in Node.list() if Node(node).chef_environment == env)

    file = open("hosts", "w")
    file.write("[hosts]\n")

    map(lambda n: file.write("{0}\n".format(Node(n)['ipaddress'])), nodes)

argh.dispatch_command(hosts)
