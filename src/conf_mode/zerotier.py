#!/usr/bin/env python3
#
# Copyright (C) 2024 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json

from vyos.config import Config
from vyos import ConfigError

def get_config():
    if config:
        conf = config
    else:
        conf = Config()

    # Base path to CLI nodes
    base = ['zerotier']
    # Convert the VyOS config to an abstract internal representation
    config_data = conf.get_config_dict(base, key_mangling=('-', '_'), get_first_key=True)

    print(json.dumps(config_data))
    return config_data

def verify(config):
    # Verify that configuration is valid
    if invalid:
        raise ConfigError("Descriptive message")
    return True

def generate(config):
    # Generate daemon configs
    pass

def apply(config):
    # Apply the generated configs to the live system
    pass

try:
    c = get_config()
    verify(c)
    generate(c)
    apply(c)
except ConfigError as e:
    print(e)
    sys.exit(1)
