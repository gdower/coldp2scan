
class DistributionCOLDP:

    taxonID = ''
    area = ''
    gazetteer = ''
    status = ''
    referenceID = ''

    def __init__(self, taxonID, area, gazetteer='', status='', referenceID=''):
        self.taxonID = taxonID
        self.area = area
        self.gazetteer = gazetteer
        self.status = status
        self.referenceID = referenceID

    def __str__(self):
        return str(self.taxonID) + '\t' + self.area + '\t' + self.gazetteer + '\t' + self.status + '\t' + \
               str(self.referenceID) + '\n'

    def __repr__(self):
        return str(self.taxonID) + '\t' + self.area + '\t' + self.gazetteer + '\t' + self.status + '\t' + \
               str(self.referenceID) + '\n'
