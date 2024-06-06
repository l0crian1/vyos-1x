#!/usr/bin/env python3
#
# Copyright (C) 2016-2024 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This script is will output various information related to ZeroTier

import sys
import typing
import json

import vyos.opmode
from vyos.utils.process import cmd
from vyos.configquery import ConfigTreeQuery

conf = ConfigTreeQuery()

def show_zerotier_summary(raw: bool, command: typing.Optional[str]):
    pass

def show_zerotier_interfaces(raw: bool, command: typing.Optional[str]):
    # Get list of interfaces
    zt_int_dict = conf.get_config_dict(['interfaces', 'zerotier'], key_mangling=('-', '_'),
                            get_first_key=True)


    # Get Node ID
    # Get IP Addresses
    # Get Networks


def show_zerotier_metrics(raw: bool, command: typing.Optional[str]):
    pass
def show_zerotier_peers(raw: bool, command: typing.Optional[str]):
    pass
def show_zerotier_local_conf(raw: bool, command: typing.Optional[str]):
    pass
def show_zerotier_bond(raw: bool, command: typing.Optional[str]):
    pass

if __name__ == '__main__':
    try:
        res = vyos.opmode.run(sys.modules[__name__])
        if res:
            print(res)
    except (ValueError, vyos.opmode.Error) as e:
        print(e)
        sys.exit(1)
