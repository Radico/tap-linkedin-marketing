from tap_kit.streams import Stream
import singer

LOGGER = singer.get_logger()


class MarketingStream(Stream):

    stream = 'marketing'

    meta_fields = dict(
        key_properties=['pivotValue'],
        replication_method='full_table',
        selected_by_default=False

    )

    schema = {
        "properties": {
            "externalWebsitePostClickConversions":{
                "type": ["null", "number"]
            },
            "adUnitClicks":{
                "type": ["null", "number"]
            },
            "companyPageClicks":{ 
                "type": ["null", "number"]
            },
            "videoFirstQuartileCompletions":{ 
                "type": ["null", "number"]
            },
            "viralOneClickLeads":{ 
                "type": ["null", "number"]
            },
            "textUrlClicks":{
                "type": ["null", "number"]
            },
            "viralCommentLikes":{
                "type": ["null", "number"]
            },
            "videoStarts":{
                "type": ["null", "number"]
            },
            "viralExternalWebsiteConversions":{
                "type": ["null", "number"]
            },
            "pivot":{
                "type": ["null", "string"]
            },
            "videoThirdQuartileCompletions":{
                "type": ["null", "number"]
            },
            "cardClicks":{
                "type": ["null", "number"]
            },
            "likes":{
                "type": ["null", "number"]
            },
            "viralComments":{
                "type": ["null", "number"]
            },
            "viralVideoThirdQuartileCompletions":{
                "type": ["null", "number"]
            },
            "oneClickLeads":{
                "type": ["null", "number"]
            },
            "fullScreenPlays":{
                "type": ["null", "number"]
            },
            "viralCardImpressions":{
                "type": ["null", "number"]
            },
            "follows":{
                "type": ["null", "number"]
            },
            "viralOneClickLeadFormOpens":{
                "type": ["null", "number"]
            },
            "conversionValueInLocalCurrency":{
                "type": ["null", "string"]
            },
            "viralFollows":{
                "type": ["null", "number"]
            },
            "otherEngagements":{
                "type": ["null", "number"]
            },
            "viralVideoCompletions":{
                "type": ["null", "number"]
            },
            "cardImpressions":{
                "type": ["null", "number"]
            },
            "leadGenerationMailInterestedClicks":{
                "type": ["null", "number"]
            },
            "opens":{
                "type": ["null", "number"]
            },
            "viralReactions":{
                "type": ["null", "number"]
            },
            "totalEngagements":{
                "type": ["null", "number"]
            },
            "videoViews":{
                "type": ["null", "number"]
            },
            "viralImpressions":{
                "type": ["null", "number"]
            },
            "viralVideoViews":{
                "type": ["null", "number"]
            },
            "dateRange": {
                "properties":{
                    "start": {
                        "properties":{
                            "month":{
                                "type": ["null", "number"]
                            },
                            "year":{
                                "type": ["null", "number"]
                            },
                            "day":{
                                "type": ["null", "number"]
                            },
                        },
                        "type": ["null", "object"]
                    },
                    "end":{
                        "properties": {
                            "month": {
                                "type": ["null", "number"]
                            },
                            "year": {
                                "type": ["null", "number"]
                            },
                            "day": {
                                "type": ["null", "number"]
                            },
                        },
                        "type": ["null", "object"]
                    }
                },
                "type": ["null", "object"]
            },
            "commentLikes":{
                "type": ["null", "number"]
            },
            "costInLocalCurrency":{
                "type": ["null", "string"]
            },
            "viralLikes":{
                "type": ["null", "number"]
            },
            "viralVideoMidpointCompletions":{
                "type": ["null", "number"]
            },
            "viralOtherEngagements":{
                "type": ["null", "number"]
            },
            "shares":{
                "type": ["null", "number"]
            },
            "viralFullScreenPlays":{
                "type": ["null", "number"]
            },
            "videoMidpointCompletions":{
                "type": ["null", "number"]
            },
            "viralCardClicks":{
                "type": ["null", "number"]
            },
            "viralExternalWebsitePostViewConversions":{
                "type": ["null", "number"]
            },
            "viralTotalEngagements":{
                "type": ["null", "number"]
            },
            "viralCompanyPageClicks":{
                "type": ["null", "number"]
            },
            "actionClicks":{
                "type": ["null", "number"]
            },
            "viralShares":{
                "type": ["null", "number"]
            },
            "videoCompletions":{
                "type": ["null", "number"]
            },
            "pivotValue":{
                "type": ["null", "string"]
            },
            "externalWebsitePostViewConversions":{
                "type": ["null", "number"]
            },
            "comments":{
                "type": ["null", "number"]
            },
            "viralVideoStarts":{
                "type": ["null", "number"]
            },
            "costInUsd":{
                "type": ["null", "string"]
            },
            "landingPageClicks":{
                "type": ["null", "number"]
            },
            "oneClickLeadFormOpens":{
                "type": ["null", "number"]
            },
            "impressions":{
                "type": ["null", "number"]
            },
            "sends":{
                "type": ["null", "number"]
            },
            "viralLandingPageClicks":{
                "type": ["null", "number"]
            },
            "viralExternalWebsitePostClickConversions":{
                "type": ["null", "number"]
            },
            "externalWebsiteConversions":{
                "type": ["null", "number"]
            },
            "viralVideoFirstQuartileCompletions":{
                "type": ["null", "number"]
            },
            "leadGenerationMailContactInfoShares":{
                "type": ["null", "number"]
            },
            "clicks":{
                "type": ["null", "number"]
            },
            "reactions":{
                "type": ["null", "number"]
            },
            "viralClicks":{
                "type": ["null", "number"]
            },
            "pivotValues":{
                "properties":{

                },
                "type": ["null", "string"]
            }
        }
    }

