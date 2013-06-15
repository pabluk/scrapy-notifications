import urllib

from scrapy import log
from scrapy import signals
from scrapy.exceptions import NotConfigured


SPIDER_NOTIFICATION_ATTRS_DEFAULT = ['name']


class SpiderNotification(object):

    def __init__(self, url, attrs):
        self.url = url
        self.attrs = attrs

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('SPIDER_NOTIFICATION_ENABLED'):
            raise NotConfigured('You must activate the SPIDER_NOTIFICATION_ENABLED setting.')

        url = crawler.settings.get('SPIDER_NOTIFICATION_URL')
        if not url:
            raise NotConfigured('You must add an URL to the SPIDER_NOTIFICATION_URL setting.')

        attrs = crawler.settings.get('SPIDER_NOTIFICATION_ATTRS')
        if not attrs:
            attrs = SPIDER_NOTIFICATION_ATTRS_DEFAULT

        ext = cls(url, attrs)

        crawler.signals.connect(ext.spider_closed,
                                signal=signals.spider_closed)

        return ext

    def spider_closed(self, spider):
        spider_attrs = {}
        for attr in self.attrs:
            spider_attrs[attr] = getattr(spider, attr)
        params = urllib.urlencode(spider_attrs)

        msg = "Sending notification for spider %s" % spider.name
        spider.log(msg, level=log.INFO)
        try:
            f = urllib.urlopen("%s?%s" % (self.url, params))
            status_code = f.getcode()
            if status_code != 200:
                msg = "Can't send notification to %s HTTP status code %d" % (self.url, status_code)
                spider.log(msg, level=log.WARNING)
        except IOError:
            msg = "Can't send notification to %s" % self.url
            spider.log(msg, level=log.WARNING)
