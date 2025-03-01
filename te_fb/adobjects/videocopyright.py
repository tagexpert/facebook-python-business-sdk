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

class VideoCopyright(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isVideoCopyright = True
        super(VideoCopyright, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        content_category = 'content_category'
        copyright_content_id = 'copyright_content_id'
        creator = 'creator'
        excluded_ownership_segments = 'excluded_ownership_segments'
        id = 'id'
        in_conflict = 'in_conflict'
        monitoring_status = 'monitoring_status'
        monitoring_type = 'monitoring_type'
        ownership_countries = 'ownership_countries'
        reference_file = 'reference_file'
        reference_file_disabled = 'reference_file_disabled'
        reference_file_disabled_by_ops = 'reference_file_disabled_by_ops'
        reference_owner_id = 'reference_owner_id'
        rule_ids = 'rule_ids'
        tags = 'tags'
        whitelisted_ids = 'whitelisted_ids'

    class ContentCategory:
        episode = 'episode'
        movie = 'movie'
        web = 'web'

    class MonitoringType:
        audio_only = 'AUDIO_ONLY'
        video_and_audio = 'VIDEO_AND_AUDIO'
        video_only = 'VIDEO_ONLY'

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
            target_class=VideoCopyright,
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

    def api_update(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'append_excluded_ownership_segments': 'bool',
            'attribution_id': 'string',
            'content_category': 'content_category_enum',
            'excluded_ownership_countries': 'list<string>',
            'excluded_ownership_segments': 'list<Object>',
            'is_reference_disabled': 'bool',
            'monitoring_type': 'monitoring_type_enum',
            'ownership_countries': 'list<string>',
            'rule_id': 'string',
            'whitelisted_ids': 'list<string>',
            'whitelisted_ig_user_ids': 'list<string>',
        }
        enums = {
            'content_category_enum': VideoCopyright.ContentCategory.__dict__.values(),
            'monitoring_type_enum': VideoCopyright.MonitoringType.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=VideoCopyright,
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

    def get_update_records(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/update_records',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
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
        'content_category': 'string',
        'copyright_content_id': 'string',
        'creator': 'User',
        'excluded_ownership_segments': 'list<VideoCopyrightSegment>',
        'id': 'string',
        'in_conflict': 'bool',
        'monitoring_status': 'string',
        'monitoring_type': 'string',
        'ownership_countries': 'VideoCopyrightGeoGate',
        'reference_file': 'CopyrightReferenceContainer',
        'reference_file_disabled': 'bool',
        'reference_file_disabled_by_ops': 'bool',
        'reference_owner_id': 'string',
        'rule_ids': 'list<VideoCopyrightRule>',
        'tags': 'list<string>',
        'whitelisted_ids': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ContentCategory'] = VideoCopyright.ContentCategory.__dict__.values()
        field_enum_info['MonitoringType'] = VideoCopyright.MonitoringType.__dict__.values()
        return field_enum_info


