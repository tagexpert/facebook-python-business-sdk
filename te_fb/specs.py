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

"""
specs module contains classes that help you define and create specs for use
in the Ads API.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from te_fb.adobjects.abstractobject  import AbstractObject
from te_fb.mixins import ValidatesFields
from te_fb.adobjects import adcreativeobjectstoryspec
from te_fb.adobjects import adcreativelinkdatachildattachment
from te_fb.adobjects import adcreativelinkdata
from te_fb.adobjects import adcreativetextdata
from te_fb.adobjects import adcreativephotodata
from te_fb.adobjects import adcreativevideodata
from te_fb.adobjects import pagepost
from te_fb.adobjects import user


class ObjectStorySpec(adcreativeobjectstoryspec.AdCreativeObjectStorySpec):
    pass


class AttachmentData(adcreativelinkdatachildattachment.AdCreativeLinkDataChildAttachment):
    pass


class LinkData(adcreativelinkdata.AdCreativeLinkData):
    pass


class TemplateData(adcreativelinkdata.AdCreativeLinkData):
    pass


class TextData(adcreativetextdata.AdCreativeTextData):
    pass


class PhotoData(adcreativephotodata.AdCreativePhotoData):
    pass


class VideoData(adcreativevideodata.AdCreativeVideoData):
    pass

class PagePostData(pagepost.PagePost):
    pass

class UserData(user.User):
    pass

class SlideshowSpec(ValidatesFields, AbstractObject):
    class Field(object):
        images_urls = 'images_urls'
        duration_ms = 'duration_ms'
        transition_ms = 'transition_ms'
