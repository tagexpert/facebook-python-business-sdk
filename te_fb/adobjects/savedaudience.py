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

class SavedAudience(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isSavedAudience = True
        super(SavedAudience, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account = 'account'
        approximate_count_lower_bound = 'approximate_count_lower_bound'
        approximate_count_upper_bound = 'approximate_count_upper_bound'
        delete_time = 'delete_time'
        description = 'description'
        extra_info = 'extra_info'
        id = 'id'
        name = 'name'
        operation_status = 'operation_status'
        page_deletion_marked_delete_time = 'page_deletion_marked_delete_time'
        permission_for_actions = 'permission_for_actions'
        run_status = 'run_status'
        sentence_lines = 'sentence_lines'
        targeting = 'targeting'
        time_created = 'time_created'
        time_updated = 'time_updated'

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
            target_class=SavedAudience,
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
        'account': 'AdAccount',
        'approximate_count_lower_bound': 'int',
        'approximate_count_upper_bound': 'int',
        'delete_time': 'int',
        'description': 'string',
        'extra_info': 'string',
        'id': 'string',
        'name': 'string',
        'operation_status': 'CustomAudienceStatus',
        'page_deletion_marked_delete_time': 'int',
        'permission_for_actions': 'AudiencePermissionForActions',
        'run_status': 'string',
        'sentence_lines': 'list',
        'targeting': 'Targeting',
        'time_created': 'datetime',
        'time_updated': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


