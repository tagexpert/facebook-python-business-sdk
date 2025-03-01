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

class AdCreativeLinkDataImageLayerSpec(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdCreativeLinkDataImageLayerSpec, self).__init__()
        self._isAdCreativeLinkDataImageLayerSpec = True
        self._api = api

    class Field(AbstractObject.Field):
        blending_mode = 'blending_mode'
        content = 'content'
        frame_image_hash = 'frame_image_hash'
        frame_source = 'frame_source'
        image_source = 'image_source'
        layer_type = 'layer_type'
        opacity = 'opacity'
        overlay_position = 'overlay_position'
        overlay_shape = 'overlay_shape'
        scale = 'scale'
        shape_color = 'shape_color'
        text_color = 'text_color'
        text_font = 'text_font'

    class BlendingMode:
        lighten = 'lighten'
        multiply = 'multiply'
        normal = 'normal'

    class FrameSource:
        custom = 'custom'

    class ImageSource:
        catalog = 'catalog'

    class LayerType:
        frame_overlay = 'frame_overlay'
        image = 'image'
        text_overlay = 'text_overlay'

    class OverlayPosition:
        bottom = 'bottom'
        bottom_left = 'bottom_left'
        bottom_right = 'bottom_right'
        center = 'center'
        left = 'left'
        right = 'right'
        top = 'top'
        top_left = 'top_left'
        top_right = 'top_right'

    class OverlayShape:
        circle = 'circle'
        none = 'none'
        pill = 'pill'
        rectangle = 'rectangle'
        triangle = 'triangle'

    class TextFont:
        droid_serif_regular = 'droid_serif_regular'
        lato_regular = 'lato_regular'
        noto_sans_regular = 'noto_sans_regular'
        nunito_sans_bold = 'nunito_sans_bold'
        open_sans_bold = 'open_sans_bold'
        open_sans_condensed_bold = 'open_sans_condensed_bold'
        pt_serif_bold = 'pt_serif_bold'
        roboto_condensed_regular = 'roboto_condensed_regular'
        roboto_medium = 'roboto_medium'

    _field_types = {
        'blending_mode': 'BlendingMode',
        'content': 'Object',
        'frame_image_hash': 'string',
        'frame_source': 'FrameSource',
        'image_source': 'ImageSource',
        'layer_type': 'LayerType',
        'opacity': 'int',
        'overlay_position': 'OverlayPosition',
        'overlay_shape': 'OverlayShape',
        'scale': 'int',
        'shape_color': 'string',
        'text_color': 'string',
        'text_font': 'TextFont',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BlendingMode'] = AdCreativeLinkDataImageLayerSpec.BlendingMode.__dict__.values()
        field_enum_info['FrameSource'] = AdCreativeLinkDataImageLayerSpec.FrameSource.__dict__.values()
        field_enum_info['ImageSource'] = AdCreativeLinkDataImageLayerSpec.ImageSource.__dict__.values()
        field_enum_info['LayerType'] = AdCreativeLinkDataImageLayerSpec.LayerType.__dict__.values()
        field_enum_info['OverlayPosition'] = AdCreativeLinkDataImageLayerSpec.OverlayPosition.__dict__.values()
        field_enum_info['OverlayShape'] = AdCreativeLinkDataImageLayerSpec.OverlayShape.__dict__.values()
        field_enum_info['TextFont'] = AdCreativeLinkDataImageLayerSpec.TextFont.__dict__.values()
        return field_enum_info


