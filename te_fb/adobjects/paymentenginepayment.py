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

class PaymentEnginePayment(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPaymentEnginePayment = True
        super(PaymentEnginePayment, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        actions = 'actions'
        application = 'application'
        country = 'country'
        created_time = 'created_time'
        disputes = 'disputes'
        fraud_status = 'fraud_status'
        fulfillment_status = 'fulfillment_status'
        id = 'id'
        is_from_ad = 'is_from_ad'
        is_from_page_post = 'is_from_page_post'
        items = 'items'
        payout_foreign_exchange_rate = 'payout_foreign_exchange_rate'
        phone_support_eligible = 'phone_support_eligible'
        platform = 'platform'
        refundable_amount = 'refundable_amount'
        request_id = 'request_id'
        tax = 'tax'
        tax_country = 'tax_country'
        test = 'test'
        user = 'user'

    class Reason:
        banned_user = 'BANNED_USER'
        denied_refund = 'DENIED_REFUND'
        granted_replacement_item = 'GRANTED_REPLACEMENT_ITEM'

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
            target_class=PaymentEnginePayment,
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

    def create_dispute(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'reason': 'reason_enum',
        }
        enums = {
            'reason_enum': PaymentEnginePayment.Reason.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/dispute',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PaymentEnginePayment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PaymentEnginePayment, api=self._api),
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

    def create_refund(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'amount': 'float',
            'currency': 'string',
            'reason': 'reason_enum',
        }
        enums = {
            'reason_enum': PaymentEnginePayment.Reason.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/refunds',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=PaymentEnginePayment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=PaymentEnginePayment, api=self._api),
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
        'actions': 'list<Object>',
        'application': 'Application',
        'country': 'string',
        'created_time': 'datetime',
        'disputes': 'list<Object>',
        'fraud_status': 'string',
        'fulfillment_status': 'string',
        'id': 'string',
        'is_from_ad': 'bool',
        'is_from_page_post': 'bool',
        'items': 'list<Object>',
        'payout_foreign_exchange_rate': 'float',
        'phone_support_eligible': 'bool',
        'platform': 'string',
        'refundable_amount': 'CurrencyAmount',
        'request_id': 'string',
        'tax': 'string',
        'tax_country': 'string',
        'test': 'unsigned int',
        'user': 'User',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Reason'] = PaymentEnginePayment.Reason.__dict__.values()
        return field_enum_info


