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

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class TargetingGeoLocationPlace(
    AbstractObject,
):

    def __init__(self, api=None):
        super(TargetingGeoLocationPlace, self).__init__()
        self._isTargetingGeoLocationPlace = True
        self._api = api

    class Field(AbstractObject.Field):
        country = 'country'
        distance_unit = 'distance_unit'
        key = 'key'
        latitude = 'latitude'
        longitude = 'longitude'
        name = 'name'
        primary_city_id = 'primary_city_id'
        radius = 'radius'
        region_id = 'region_id'

    _field_types = {
        'country': 'string',
        'distance_unit': 'string',
        'key': 'string',
        'latitude': 'float',
        'longitude': 'float',
        'name': 'string',
        'primary_city_id': 'int',
        'radius': 'float',
        'region_id': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


