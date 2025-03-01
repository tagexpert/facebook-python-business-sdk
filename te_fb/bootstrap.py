# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sys
import os

this_dir = os.path.dirname(__file__)
repo_dir = os.path.join(this_dir, os.pardir)
sys.path.insert(1, repo_dir)

import json
from te_fb.session import FacebookSession
from te_fb.api import FacebookAdsApi
from te_fb.adobjects import *
from te_fb.exceptions import FacebookError


class Authentication():
    """
        DON'T USE THIS CLASS DIRECTLY. USE `auth()` function from this module
        Helper class to authenticate using config.json config file from this
        repository. This is useful in two cases:
            - Testing environment
            - Interactive exploration in REPL
        This class shouldn't be used in production.
        It's intended for development. Use FacebookAdsApi.init in production
    """

    _api = FacebookAdsApi.get_default_api()
    if _api:
        _is_authenticated = True
    else:
        _is_authenticated = False

    @property
    def is_authenticated(cls):
        return cls._is_authenticated

    @classmethod
    def load_config(cls):
        config_file = open(os.path.join(repo_dir, 'config.json'))
        config = json.load(config_file)
        config_file.close()
        return config

    @classmethod
    def auth(cls):
        """
            Prepare for Ads API calls and return a tuple with act_id
            and page_id. page_id can be None but act_id is always set.
        """
        config = cls.load_config()

        if cls._is_authenticated:
            return config['act_id'], config.get('page_id', None)

        if config['app_id'] and config['app_secret'] \
           and config['act_id'] and config['access_token']:

            FacebookAdsApi.init(
                config['app_id'],
                config['app_secret'],
                config['access_token'],
                config['act_id'],
            )

            cls._is_authenticated = True

            return config['act_id'], config.get('page_id', None)

        else:
            required_fields = set(
                ('app_id', 'app_secret', 'act_id', 'access_token')
            )

            missing_fields = required_fields - set(config.keys())
            raise FacebookError(
                '\n\tFile config.json needs to have the following fields: {}\n'
                '\tMissing fields: {}\n'.format(
                    ', '.join(required_fields),
                    ', '.join(missing_fields),
                )
            )


def auth():
    return Authentication.auth()

if sys.flags.interactive:
    auth()
