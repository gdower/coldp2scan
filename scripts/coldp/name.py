
class NameCOLDP:

    def __init__(self, ID,
                 scientificName,
                 authorship='',
                 rank='',
                 genus='',
                 infragenericEpithet='',
                 specificEpithet='',
                 infraspecificEpithet='',
                 publishedInID='',
                 publishedInPage='',
                 publishedInYear='',
                 original='',
                 code='',
                 status='',
                 link='',
                 remarks=''):
        self.ID = ID
        self.scientificName = scientificName
        self.authorship = authorship
        self.rank = rank
        self.genus = genus
        self.infragenericEpithet = infragenericEpithet
        self.specificEpithet = specificEpithet
        self.infraspecificEpithet = infraspecificEpithet
        self.publishedInID = publishedInID
        self.publishedInPage = publishedInPage
        self.publishedInYear = publishedInYear
        self.original = original
        self.code = code
        self.status = status
        self.link = link
        self.remarks = remarks
        self.parents = {'order': '',
                        'nanorder': '',
                        'suborder': '',
                        'infraorder': '',
                        'parvorder': '',
                        'superfamily': '',
                        'family': '',
                        'subfamily': '',
                        'genus': '',
                        'subgenus': '',
                        'superspecies': '',
                        'subsuperspecies': '',
                        'species': '',
                        'subspecies': '',
                        'tribe': '',
                        'subtribe': ''}

    def __str__(self):
        return str(self.ID) + '\t' + \
               str(self.scientificName) + '\t' + \
               str(self.authorship) + '\t' + \
               str(self.rank) + '\t' + \
               str(self.genus) + '\t' + \
               str(self.infragenericEpithet) + '\t' + \
               str(self.specificEpithet) + '\t' + \
               str(self.infraspecificEpithet) + '\t' + \
               str(self.publishedInID) + '\t' + \
               str(self.publishedInPage) + '\t' + \
               str(self.publishedInYear) + '\t' + \
               str(self.original) + '\t' + \
               str(self.code) + '\t' + \
               str(self.status) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\n'

    def __repr__(self):
        return str(self.ID) + '\t' + \
               str(self.scientificName) + '\t' + \
               str(self.authorship) + '\t' + \
               str(self.rank) + '\t' + \
               str(self.genus) + '\t' + \
               str(self.infragenericEpithet) + '\t' + \
               str(self.specificEpithet) + '\t' + \
               str(self.infraspecificEpithet) + '\t' + \
               str(self.publishedInID) + '\t' + \
               str(self.publishedInPage) + '\t' + \
               str(self.publishedInYear) + '\t' + \
               str(self.original) + '\t' + \
               str(self.code) + '\t' + \
               str(self.status) + '\t' + \
               str(self.link) + '\t' + \
               str(self.remarks) + '\n'

    def add_parent(self, key, value):
        self.parents[key] = value
