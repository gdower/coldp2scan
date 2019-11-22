
class ReferenceCOLDP:

    def __init__(self, ID, citation='', author='', title='', year='', source='', doi='', link=''):
        self.ID = ID
        self.citation = citation
        self.author = author
        self.title = title
        self.year = year
        self.source = source
        self.doi = doi
        self.link = link

    def __str__(self):
        return str(self.ID) + '\t' + self.citation + '\t' + self.author + '\t' + self.title + '\t' + \
               self.year + '\t' + self.source + '\t' + self.doi + '\t' + self.link + '\n'

    def __repr__(self):
        return str(self.ID) + '\t' + self.citation + '\t' + self.author + '\t' + self.title + '\t' + \
               self.year + '\t' + self.source + '\t' + self.doi + '\t' + self.link + '\n'
