#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2000-2008 Bastian Kleineidam
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sys
import cgi
import linkcheck
import linkcheck.lc_cgi


# log errors to stdout
sys.stderr = sys.stdout

# List of IP numbers that are allowed to use the CGI interface.
# This gets compared with the REMOTE_ADDR environment variable of the CGI
# request.
ALLOWED_CLIENTS = ['127.0.0.1']
# List of IP numbers that are allowed to function as the server.
# This gets compared with the SERVER_ADDR environment variable of the CGI
# request.
ALLOWED_SERVERS = ['127.0.0.1']
# uncomment the following lines to test your CGI values
#cgi.test()
#sys.exit(0)
linkcheck.lc_cgi.startoutput()
if linkcheck.lc_cgi.checkaccess(allowed_clients=ALLOWED_CLIENTS,
                                allowed_servers=ALLOWED_SERVERS):
    linkcheck.lc_cgi.checklink(form=cgi.FieldStorage())
