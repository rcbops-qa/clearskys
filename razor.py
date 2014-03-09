#!/usr/bin/env python

import sys
import argh
import requests


class Razor():

    def __init__(self, url):
        self.url = url

    def delete(self, node):
        """
        Deletes a given node
        :param node: Razor node name to destroy
        :type node: string
        """

        # Call the Razor RESTful API to get a node
        headers = {'content-type': 'application/json'}
        data = '{{"name": "{0}"}}'.format(node)
        r = requests.post('{0}/commands/delete-node'.format(self.url),
                          headers=headers, data=data)

        # Check the status code and return appropriately
        if r.status_code == 202 and 'no changes' not in r.content
            print r.status_code
            print r.content
        else:
            sys.stderr.write(str(r.status_code) + "\n" + r.content + "\n")
            sys.exit(1)

def delete_node(url, node):
    razor = Razor(url)
    razor.delete(node)

argh.dispatch_command(delete_node)
