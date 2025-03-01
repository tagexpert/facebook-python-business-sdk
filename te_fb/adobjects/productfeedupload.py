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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductFeedUpload(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeedUpload = True
        super(ProductFeedUpload, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        end_time = 'end_time'
        error_count = 'error_count'
        error_report = 'error_report'
        filename = 'filename'
        id = 'id'
        input_method = 'input_method'
        num_deleted_items = 'num_deleted_items'
        num_detected_items = 'num_detected_items'
        num_invalid_items = 'num_invalid_items'
        num_persisted_items = 'num_persisted_items'
        start_time = 'start_time'
        url = 'url'
        warning_count = 'warning_count'

    class InputMethod:
        google_sheets_fetch = 'Google Sheets Fetch'
        manual_upload = 'Manual Upload'
        reupload_last_file = 'Reupload Last File'
        server_fetch = 'Server Fetch'
        user_initiated_server_fetch = 'User initiated server fetch'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'uploads'

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
            target_class=ProductFeedUpload,
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

    def create_error_report(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/error_report',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeedUpload,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeedUpload, api=self._api),
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

    def get_errors(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.productfeeduploaderror import ProductFeedUploadError
        param_types = {
            'error_priority': 'error_priority_enum',
        }
        enums = {
            'error_priority_enum': ProductFeedUploadError.ErrorPriority.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/errors',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ProductFeedUploadError,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ProductFeedUploadError, api=self._api),
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
        'end_time': 'datetime',
        'error_count': 'int',
        'error_report': 'ProductFeedUploadErrorReport',
        'filename': 'string',
        'id': 'string',
        'input_method': 'InputMethod',
        'num_deleted_items': 'int',
        'num_detected_items': 'int',
        'num_invalid_items': 'int',
        'num_persisted_items': 'int',
        'start_time': 'datetime',
        'url': 'string',
        'warning_count': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['InputMethod'] = ProductFeedUpload.InputMethod.__dict__.values()
        return field_enum_info


