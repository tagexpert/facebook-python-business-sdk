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

class ExtendedCredit(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isExtendedCredit = True
        super(ExtendedCredit, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        allocated_amount = 'allocated_amount'
        balance = 'balance'
        credit_available = 'credit_available'
        credit_type = 'credit_type'
        id = 'id'
        is_access_revoked = 'is_access_revoked'
        is_automated_experience = 'is_automated_experience'
        legal_entity_name = 'legal_entity_name'
        liable_biz_name = 'liable_biz_name'
        max_balance = 'max_balance'
        online_max_balance = 'online_max_balance'
        owner_business = 'owner_business'
        owner_business_name = 'owner_business_name'
        partition_from = 'partition_from'
        receiving_credit_allocation_config = 'receiving_credit_allocation_config'
        send_bill_to_biz_name = 'send_bill_to_biz_name'

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
            target_class=ExtendedCredit,
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

    def get_extended_credit_invoice_groups(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/extended_credit_invoice_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditInvoiceGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCreditInvoiceGroup, api=self._api),
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

    def create_extended_credit_invoice_group(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.extendedcreditinvoicegroup import ExtendedCreditInvoiceGroup
        param_types = {
            'emails': 'list<string>',
            'name': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/extended_credit_invoice_groups',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditInvoiceGroup,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCreditInvoiceGroup, api=self._api),
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

    def get_owning_credit_allocation_configs(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.extendedcreditallocationconfig import ExtendedCreditAllocationConfig
        param_types = {
            'receiving_business_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/owning_credit_allocation_configs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditAllocationConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCreditAllocationConfig, api=self._api),
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

    def create_owning_credit_allocation_config(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.extendedcreditallocationconfig import ExtendedCreditAllocationConfig
        param_types = {
            'amount': 'Object',
            'liability_type': 'liability_type_enum',
            'partition_type': 'partition_type_enum',
            'receiving_business_id': 'string',
            'send_bill_to': 'send_bill_to_enum',
        }
        enums = {
            'liability_type_enum': ExtendedCreditAllocationConfig.LiabilityType.__dict__.values(),
            'partition_type_enum': ExtendedCreditAllocationConfig.PartitionType.__dict__.values(),
            'send_bill_to_enum': ExtendedCreditAllocationConfig.SendBillTo.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/owning_credit_allocation_configs',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditAllocationConfig,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=ExtendedCreditAllocationConfig, api=self._api),
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

    def create_whatsapp_credit_sharing_and_attach(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'waba_currency': 'string',
            'waba_id': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/whatsapp_credit_sharing_and_attach',
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
        'allocated_amount': 'CurrencyAmount',
        'balance': 'CurrencyAmount',
        'credit_available': 'CurrencyAmount',
        'credit_type': 'string',
        'id': 'string',
        'is_access_revoked': 'bool',
        'is_automated_experience': 'bool',
        'legal_entity_name': 'string',
        'liable_biz_name': 'string',
        'max_balance': 'CurrencyAmount',
        'online_max_balance': 'CurrencyAmount',
        'owner_business': 'Business',
        'owner_business_name': 'string',
        'partition_from': 'string',
        'receiving_credit_allocation_config': 'ExtendedCreditAllocationConfig',
        'send_bill_to_biz_name': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


