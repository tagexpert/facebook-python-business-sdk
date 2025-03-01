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

class ChatPlugin(
    AbstractObject,
):

    def __init__(self, api=None):
        super(ChatPlugin, self).__init__()
        self._isChatPlugin = True
        self._api = api

    class Field(AbstractObject.Field):
        alignment = 'alignment'
        desktop_bottom_spacing = 'desktop_bottom_spacing'
        desktop_side_spacing = 'desktop_side_spacing'
        entry_point_icon = 'entry_point_icon'
        entry_point_label = 'entry_point_label'
        greeting_dialog_display = 'greeting_dialog_display'
        guest_chat_mode = 'guest_chat_mode'
        mobile_bottom_spacing = 'mobile_bottom_spacing'
        mobile_chat_display = 'mobile_chat_display'
        mobile_side_spacing = 'mobile_side_spacing'
        theme_color = 'theme_color'
        welcome_screen_greeting = 'welcome_screen_greeting'

    _field_types = {
        'alignment': 'string',
        'desktop_bottom_spacing': 'string',
        'desktop_side_spacing': 'string',
        'entry_point_icon': 'string',
        'entry_point_label': 'string',
        'greeting_dialog_display': 'string',
        'guest_chat_mode': 'string',
        'mobile_bottom_spacing': 'string',
        'mobile_chat_display': 'string',
        'mobile_side_spacing': 'string',
        'theme_color': 'string',
        'welcome_screen_greeting': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


