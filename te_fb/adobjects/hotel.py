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

class Hotel(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isHotel = True
        super(Hotel, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        applinks = 'applinks'
        brand = 'brand'
        category = 'category'
        category_specific_fields = 'category_specific_fields'
        currency = 'currency'
        description = 'description'
        guest_ratings = 'guest_ratings'
        hotel_id = 'hotel_id'
        id = 'id'
        image_fetch_status = 'image_fetch_status'
        images = 'images'
        lowest_base_price = 'lowest_base_price'
        loyalty_program = 'loyalty_program'
        margin_level = 'margin_level'
        name = 'name'
        phone = 'phone'
        sale_price = 'sale_price'
        sanitized_images = 'sanitized_images'
        star_rating = 'star_rating'
        unit_price = 'unit_price'
        url = 'url'
        base_price = 'base_price'

    class ImageFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'hotels'

    # @deprecated api_create is being deprecated
    def api_create(self, parent_id, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.adobjects.productcatalog import ProductCatalog
        return ProductCatalog(api=self._api, fbid=parent_id).create_hotel(fields, params, batch, success, failure, pending)

    def api_delete(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
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
            target_class=Hotel,
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
            'address': 'Object',
            'applinks': 'Object',
            'base_price': 'unsigned int',
            'brand': 'string',
            'currency': 'string',
            'description': 'string',
            'guest_ratings': 'list<Object>',
            'images': 'list<Object>',
            'name': 'string',
            'phone': 'string',
            'star_rating': 'float',
            'url': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Hotel,
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

    def get_augmented_realities_metadata(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/augmented_realities_metadata',
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

    def get_channels_to_integrity_status(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.catalogitemchannelstointegritystatus import CatalogItemChannelsToIntegrityStatus
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/channels_to_integrity_status',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=CatalogItemChannelsToIntegrityStatus,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=CatalogItemChannelsToIntegrityStatus, api=self._api),
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

    def get_hotel_rooms(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.hotelroom import HotelRoom
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/hotel_rooms',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=HotelRoom,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=HotelRoom, api=self._api),
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

    def get_videos_metadata(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/videos_metadata',
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
        'address': 'string',
        'applinks': 'CatalogItemAppLinks',
        'brand': 'string',
        'category': 'string',
        'category_specific_fields': 'CatalogSubVerticalList',
        'currency': 'string',
        'description': 'string',
        'guest_ratings': 'string',
        'hotel_id': 'string',
        'id': 'string',
        'image_fetch_status': 'ImageFetchStatus',
        'images': 'list<string>',
        'lowest_base_price': 'string',
        'loyalty_program': 'string',
        'margin_level': 'unsigned int',
        'name': 'string',
        'phone': 'string',
        'sale_price': 'string',
        'sanitized_images': 'list<string>',
        'star_rating': 'float',
        'unit_price': 'Object',
        'url': 'string',
        'base_price': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['ImageFetchStatus'] = Hotel.ImageFetchStatus.__dict__.values()
        return field_enum_info


