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

from te_fb.adobjects.abstractobject import AbstractObject
from te_fb.adobjects.abstractcrudobject import AbstractCrudObject
from te_fb.adobjects.objectparser import ObjectParser
from te_fb.api import FacebookRequest
from te_fb.typechecker import TypeChecker
from te_fb.adobjects.helpers.adimagemixin import AdImageMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdImage(
    AdImageMixin,
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdImage = True
        super(AdImage, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        created_time = 'created_time'
        creatives = 'creatives'
        hash = 'hash'
        height = 'height'
        id = 'id'
        is_associated_creatives_in_adgroups = 'is_associated_creatives_in_adgroups'
        name = 'name'
        original_height = 'original_height'
        original_width = 'original_width'
        permalink_url = 'permalink_url'
        status = 'status'
        updated_time = 'updated_time'
        url = 'url'
        url_128 = 'url_128'
        width = 'width'
        bytes = 'bytes'
        copy_from = 'copy_from'
        filename = 'filename'

    class Status:
        active = 'ACTIVE'
        deleted = 'DELETED'
        internal = 'INTERNAL'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'adimages'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.adobjects.adaccount import AdAccount
        return AdAccount(api=self._api, fbid=parent_id).create_ad_image(fields, params, batch, success, failure, pending)

    def api_get(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AdImage,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch, success=success, failure=failure)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'account_id': 'string',
        'created_time': 'datetime',
        'creatives': 'list<string>',
        'hash': 'string',
        'height': 'unsigned int',
        'id': 'string',
        'is_associated_creatives_in_adgroups': 'bool',
        'name': 'string',
        'original_height': 'unsigned int',
        'original_width': 'unsigned int',
        'permalink_url': 'string',
        'status': 'Status',
        'updated_time': 'datetime',
        'url': 'string',
        'url_128': 'string',
        'width': 'unsigned int',
        'bytes': 'Object',
        'copy_from': 'Object',
        'filename': 'file'
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Status'] = AdImage.Status.__dict__.values()
        return field_enum_info


