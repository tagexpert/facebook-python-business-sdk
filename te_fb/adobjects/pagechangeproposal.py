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

class PageChangeProposal(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPageChangeProposal = True
        super(PageChangeProposal, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        acceptance_status = 'acceptance_status'
        category = 'category'
        current_value = 'current_value'
        id = 'id'
        proposed_value = 'proposed_value'
        upcoming_change_info = 'upcoming_change_info'

    _field_types = {
        'acceptance_status': 'string',
        'category': 'string',
        'current_value': 'string',
        'id': 'string',
        'proposed_value': 'string',
        'upcoming_change_info': 'PageUpcomingChange',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


