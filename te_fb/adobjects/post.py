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

class Post(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isPost = True
        super(Post, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        actions = 'actions'
        admin_creator = 'admin_creator'
        allowed_advertising_objectives = 'allowed_advertising_objectives'
        application = 'application'
        backdated_time = 'backdated_time'
        call_to_action = 'call_to_action'
        can_reply_privately = 'can_reply_privately'
        caption = 'caption'
        child_attachments = 'child_attachments'
        comments_mirroring_domain = 'comments_mirroring_domain'
        coordinates = 'coordinates'
        created_time = 'created_time'
        description = 'description'
        event = 'event'
        expanded_height = 'expanded_height'
        expanded_width = 'expanded_width'
        feed_targeting = 'feed_targeting'
        field_from = 'from'
        full_picture = 'full_picture'
        height = 'height'
        icon = 'icon'
        id = 'id'
        instagram_eligibility = 'instagram_eligibility'
        is_app_share = 'is_app_share'
        is_eligible_for_promotion = 'is_eligible_for_promotion'
        is_expired = 'is_expired'
        is_hidden = 'is_hidden'
        is_inline_created = 'is_inline_created'
        is_instagram_eligible = 'is_instagram_eligible'
        is_popular = 'is_popular'
        is_published = 'is_published'
        is_spherical = 'is_spherical'
        link = 'link'
        message = 'message'
        message_tags = 'message_tags'
        multi_share_end_card = 'multi_share_end_card'
        multi_share_optimized = 'multi_share_optimized'
        name = 'name'
        object_id = 'object_id'
        parent_id = 'parent_id'
        permalink_url = 'permalink_url'
        picture = 'picture'
        place = 'place'
        privacy = 'privacy'
        promotable_id = 'promotable_id'
        promotion_status = 'promotion_status'
        properties = 'properties'
        scheduled_publish_time = 'scheduled_publish_time'
        shares = 'shares'
        source = 'source'
        status_type = 'status_type'
        story = 'story'
        story_tags = 'story_tags'
        subscribed = 'subscribed'
        target = 'target'
        targeting = 'targeting'
        timeline_visibility = 'timeline_visibility'
        type = 'type'
        updated_time = 'updated_time'
        via = 'via'
        video_buying_eligibility = 'video_buying_eligibility'
        width = 'width'

    class BackdatedTimeGranularity:
        day = 'day'
        hour = 'hour'
        min = 'min'
        month = 'month'
        none = 'none'
        year = 'year'

    class CheckinEntryPoint:
        branding_checkin = 'BRANDING_CHECKIN'
        branding_other = 'BRANDING_OTHER'
        branding_photo = 'BRANDING_PHOTO'
        branding_status = 'BRANDING_STATUS'

    class Formatting:
        markdown = 'MARKDOWN'
        plaintext = 'PLAINTEXT'

    class PlaceAttachmentSetting:
        value_1 = '1'
        value_2 = '2'

    class PostSurfacesBlacklist:
        value_1 = '1'
        value_2 = '2'
        value_3 = '3'
        value_4 = '4'
        value_5 = '5'

    class PostingToRedspace:
        disabled = 'disabled'
        enabled = 'enabled'

    class TargetSurface:
        story = 'STORY'
        timeline = 'TIMELINE'

    class UnpublishedContentType:
        ads_post = 'ADS_POST'
        draft = 'DRAFT'
        inline_created = 'INLINE_CREATED'
        published = 'PUBLISHED'
        reviewable_branded_content = 'REVIEWABLE_BRANDED_CONTENT'
        scheduled = 'SCHEDULED'
        scheduled_recurring = 'SCHEDULED_RECURRING'

    class FeedStoryVisibility:
        hidden = 'hidden'
        visible = 'visible'

    class TimelineVisibility:
        forced_allow = 'forced_allow'
        hidden = 'hidden'
        normal = 'normal'

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
            target_class=Post,
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
            'attached_media': 'list<Object>',
            'backdated_time': 'datetime',
            'backdated_time_granularity': 'backdated_time_granularity_enum',
            'composer_session_id': 'string',
            'direct_share_status': 'unsigned int',
            'explicitly_added_mentionee_ids': 'list<unsigned int>',
            'feed_story_visibility': 'feed_story_visibility_enum',
            'is_explicit_location': 'bool',
            'is_hidden': 'bool',
            'is_pinned': 'bool',
            'is_published': 'bool',
            'message': 'string',
            'og_action_type_id': 'string',
            'og_hide_object_attachment': 'bool',
            'og_icon_id': 'string',
            'og_object_id': 'string',
            'og_phrase': 'string',
            'og_set_profile_badge': 'bool',
            'og_suggestion_mechanism': 'string',
            'place': 'Object',
            'privacy': 'string',
            'product_item': 'Object',
            'scheduled_publish_time': 'unsigned int',
            'should_sync_product_edit': 'bool',
            'source_type': 'string',
            'sponsor_id': 'string',
            'sponsor_relationship': 'unsigned int',
            'tags': 'list<int>',
            'text_format_preset_id': 'string',
            'timeline_visibility': 'timeline_visibility_enum',
            'tracking': 'string',
        }
        enums = {
            'backdated_time_granularity_enum': Post.BackdatedTimeGranularity.__dict__.values(),
            'feed_story_visibility_enum': Post.FeedStoryVisibility.__dict__.values(),
            'timeline_visibility_enum': Post.TimelineVisibility.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
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

    def get_attachments(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/attachments',
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

    def get_comments(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.comment import Comment
        param_types = {
            'filter': 'filter_enum',
            'live_filter': 'live_filter_enum',
            'order': 'order_enum',
            'since': 'datetime',
        }
        enums = {
            'filter_enum': Comment.Filter.__dict__.values(),
            'live_filter_enum': Comment.LiveFilter.__dict__.values(),
            'order_enum': Comment.Order.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def create_comment(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.comment import Comment
        param_types = {
            'attachment_id': 'string',
            'attachment_share_url': 'string',
            'attachment_url': 'string',
            'comment': 'string',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'feedback_source': 'string',
            'message': 'string',
            'nectar_module': 'string',
            'parent_comment_id': 'Object',
            'post_id': 'string',
            'tracking': 'string',
        }
        enums = {
            'comment_privacy_value_enum': Comment.CommentPrivacyValue.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
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

    def get_dynamic_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.rtbdynamicpost import RTBDynamicPost
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/dynamic_posts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=RTBDynamicPost,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=RTBDynamicPost, api=self._api),
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

    def get_insights(self, fields=None, params=None, is_async=False, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.insightsresult import InsightsResult
        if is_async:
          return self.get_insights_async(fields, params, batch, success, failure, pending)
        param_types = {
            'date_preset': 'date_preset_enum',
            'metric': 'list<Object>',
            'period': 'period_enum',
            'since': 'datetime',
            'until': 'datetime',
        }
        enums = {
            'date_preset_enum': InsightsResult.DatePreset.__dict__.values(),
            'period_enum': InsightsResult.Period.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/insights',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=InsightsResult,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=InsightsResult, api=self._api),
            include_summary=False,
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

    def delete_likes(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'nectar_module': 'string',
            'tracking': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/likes',
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

    def create_like(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        param_types = {
            'feedback_source': 'string',
            'nectar_module': 'string',
            'tracking': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Post, api=self._api),
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

    def get_reactions(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.profile import Profile
        param_types = {
            'type': 'type_enum',
        }
        enums = {
            'type_enum': Profile.Type.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/reactions',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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

    def get_shared_posts(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
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
            endpoint='/sharedposts',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Post,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Post, api=self._api),
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

    def get_sponsor_tags(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.page import Page
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/sponsor_tags',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Page,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Page, api=self._api),
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

    def get_to(self, fields=None, params=None, batch=None, success=None, failure=None, pending=False):
        from te_fb.utils import api_utils
        if batch is None and (success is not None or failure is not None):
          api_utils.warning('`success` and `failure` callback only work for batch call.')
        from te_fb.adobjects.profile import Profile
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/to',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Profile,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Profile, api=self._api),
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
        'actions': 'list',
        'admin_creator': 'Object',
        'allowed_advertising_objectives': 'list<string>',
        'application': 'Application',
        'backdated_time': 'datetime',
        'call_to_action': 'Object',
        'can_reply_privately': 'bool',
        'caption': 'string',
        'child_attachments': 'list',
        'comments_mirroring_domain': 'string',
        'coordinates': 'Object',
        'created_time': 'datetime',
        'description': 'string',
        'event': 'Event',
        'expanded_height': 'unsigned int',
        'expanded_width': 'unsigned int',
        'feed_targeting': 'Object',
        'from': 'Object',
        'full_picture': 'string',
        'height': 'unsigned int',
        'icon': 'string',
        'id': 'string',
        'instagram_eligibility': 'string',
        'is_app_share': 'bool',
        'is_eligible_for_promotion': 'bool',
        'is_expired': 'bool',
        'is_hidden': 'bool',
        'is_inline_created': 'bool',
        'is_instagram_eligible': 'bool',
        'is_popular': 'bool',
        'is_published': 'bool',
        'is_spherical': 'bool',
        'link': 'Object',
        'message': 'string',
        'message_tags': 'list',
        'multi_share_end_card': 'bool',
        'multi_share_optimized': 'bool',
        'name': 'string',
        'object_id': 'string',
        'parent_id': 'string',
        'permalink_url': 'Object',
        'picture': 'string',
        'place': 'Place',
        'privacy': 'Privacy',
        'promotable_id': 'string',
        'promotion_status': 'string',
        'properties': 'list',
        'scheduled_publish_time': 'float',
        'shares': 'Object',
        'source': 'string',
        'status_type': 'string',
        'story': 'string',
        'story_tags': 'list',
        'subscribed': 'bool',
        'target': 'Profile',
        'targeting': 'Object',
        'timeline_visibility': 'string',
        'type': 'string',
        'updated_time': 'datetime',
        'via': 'Object',
        'video_buying_eligibility': 'list<string>',
        'width': 'unsigned int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['BackdatedTimeGranularity'] = Post.BackdatedTimeGranularity.__dict__.values()
        field_enum_info['CheckinEntryPoint'] = Post.CheckinEntryPoint.__dict__.values()
        field_enum_info['Formatting'] = Post.Formatting.__dict__.values()
        field_enum_info['PlaceAttachmentSetting'] = Post.PlaceAttachmentSetting.__dict__.values()
        field_enum_info['PostSurfacesBlacklist'] = Post.PostSurfacesBlacklist.__dict__.values()
        field_enum_info['PostingToRedspace'] = Post.PostingToRedspace.__dict__.values()
        field_enum_info['TargetSurface'] = Post.TargetSurface.__dict__.values()
        field_enum_info['UnpublishedContentType'] = Post.UnpublishedContentType.__dict__.values()
        field_enum_info['FeedStoryVisibility'] = Post.FeedStoryVisibility.__dict__.values()
        field_enum_info['TimelineVisibility'] = Post.TimelineVisibility.__dict__.values()
        return field_enum_info


