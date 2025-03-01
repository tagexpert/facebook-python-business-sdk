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

class AdNetworkAnalyticsSyncQueryResult(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdNetworkAnalyticsSyncQueryResult, self).__init__()
        self._isAdNetworkAnalyticsSyncQueryResult = True
        self._api = api

    class Field(AbstractObject.Field):
        query_id = 'query_id'
        results = 'results'

    class AggregationPeriod:
        day = 'DAY'
        total = 'TOTAL'

    class Breakdowns:
        ad_server_campaign_id = 'AD_SERVER_CAMPAIGN_ID'
        ad_space = 'AD_SPACE'
        age = 'AGE'
        app = 'APP'
        clicked_view_tag = 'CLICKED_VIEW_TAG'
        country = 'COUNTRY'
        deal = 'DEAL'
        deal_ad = 'DEAL_AD'
        deal_page = 'DEAL_PAGE'
        delivery_method = 'DELIVERY_METHOD'
        display_format = 'DISPLAY_FORMAT'
        fail_reason = 'FAIL_REASON'
        gender = 'GENDER'
        instant_article_id = 'INSTANT_ARTICLE_ID'
        instant_article_page_id = 'INSTANT_ARTICLE_PAGE_ID'
        is_deal_backfill = 'IS_DEAL_BACKFILL'
        placement = 'PLACEMENT'
        placement_name = 'PLACEMENT_NAME'
        platform = 'PLATFORM'
        property = 'PROPERTY'
        sdk_version = 'SDK_VERSION'

    class Metrics:
        fb_ad_network_bidding_bid_rate = 'FB_AD_NETWORK_BIDDING_BID_RATE'
        fb_ad_network_bidding_request = 'FB_AD_NETWORK_BIDDING_REQUEST'
        fb_ad_network_bidding_response = 'FB_AD_NETWORK_BIDDING_RESPONSE'
        fb_ad_network_bidding_revenue = 'FB_AD_NETWORK_BIDDING_REVENUE'
        fb_ad_network_bidding_win_rate = 'FB_AD_NETWORK_BIDDING_WIN_RATE'
        fb_ad_network_click = 'FB_AD_NETWORK_CLICK'
        fb_ad_network_cpm = 'FB_AD_NETWORK_CPM'
        fb_ad_network_ctr = 'FB_AD_NETWORK_CTR'
        fb_ad_network_filled_request = 'FB_AD_NETWORK_FILLED_REQUEST'
        fb_ad_network_fill_rate = 'FB_AD_NETWORK_FILL_RATE'
        fb_ad_network_imp = 'FB_AD_NETWORK_IMP'
        fb_ad_network_impression_rate = 'FB_AD_NETWORK_IMPRESSION_RATE'
        fb_ad_network_request = 'FB_AD_NETWORK_REQUEST'
        fb_ad_network_revenue = 'FB_AD_NETWORK_REVENUE'
        fb_ad_network_show_rate = 'FB_AD_NETWORK_SHOW_RATE'
        fb_ad_network_video_guarantee_revenue = 'FB_AD_NETWORK_VIDEO_GUARANTEE_REVENUE'
        fb_ad_network_video_mrc = 'FB_AD_NETWORK_VIDEO_MRC'
        fb_ad_network_video_mrc_rate = 'FB_AD_NETWORK_VIDEO_MRC_RATE'
        fb_ad_network_video_view = 'FB_AD_NETWORK_VIDEO_VIEW'
        fb_ad_network_video_view_rate = 'FB_AD_NETWORK_VIDEO_VIEW_RATE'

    class OrderingColumn:
        metric = 'METRIC'
        time = 'TIME'
        value = 'VALUE'

    class OrderingType:
        ascending = 'ASCENDING'
        descending = 'DESCENDING'

    _field_types = {
        'query_id': 'string',
        'results': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AggregationPeriod'] = AdNetworkAnalyticsSyncQueryResult.AggregationPeriod.__dict__.values()
        field_enum_info['Breakdowns'] = AdNetworkAnalyticsSyncQueryResult.Breakdowns.__dict__.values()
        field_enum_info['Metrics'] = AdNetworkAnalyticsSyncQueryResult.Metrics.__dict__.values()
        field_enum_info['OrderingColumn'] = AdNetworkAnalyticsSyncQueryResult.OrderingColumn.__dict__.values()
        field_enum_info['OrderingType'] = AdNetworkAnalyticsSyncQueryResult.OrderingType.__dict__.values()
        return field_enum_info


