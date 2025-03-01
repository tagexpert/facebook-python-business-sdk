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

class PartnerStudy(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPartnerStudy = True
        super(PartnerStudy, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_info = 'additional_info'
        brand = 'brand'
        client_name = 'client_name'
        emails = 'emails'
        id = 'id'
        input_ids = 'input_ids'
        is_export = 'is_export'
        lift_study = 'lift_study'
        location = 'location'
        match_file_ds = 'match_file_ds'
        name = 'name'
        partner_defined_id = 'partner_defined_id'
        partner_household_graph_dataset_id = 'partner_household_graph_dataset_id'
        status = 'status'
        study_end_date = 'study_end_date'
        study_start_date = 'study_start_date'
        study_type = 'study_type'
        submit_date = 'submit_date'

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
            target_class=PartnerStudy,
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
        'additional_info': 'string',
        'brand': 'string',
        'client_name': 'string',
        'emails': 'string',
        'id': 'string',
        'input_ids': 'list<string>',
        'is_export': 'bool',
        'lift_study': 'AdStudy',
        'location': 'string',
        'match_file_ds': 'string',
        'name': 'string',
        'partner_defined_id': 'string',
        'partner_household_graph_dataset_id': 'string',
        'status': 'string',
        'study_end_date': 'datetime',
        'study_start_date': 'datetime',
        'study_type': 'string',
        'submit_date': 'datetime',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


