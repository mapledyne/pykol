import kolala
import kolala.pagetypes as pagetypes


class PageSelector(object):

    def __init__(self, response):
        self.response = response

    def page(self):
        page_name = self.response.url.replace(kolala.Globals.url, '').split('?')[0]

        for page in pagetypes.KoLPage.__subclasses__():
            if page.claim(self.response):
                kolala.Logging.debug('Page claimed by: ' + page.__name__)
                return page(self.response)
        kolala.Logging.info('Page ({}) went unclaimed.'.format(page_name))
        return pagetypes.KoLPage(self.response)
