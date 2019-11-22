
class SynonymCOLDP:

    def __init__(self, taxonID, nameID, status='synonym', remarks=''):
        self.taxonID = taxonID
        self.nameID = nameID
        self.status = status
        self.remarks = remarks

    def __str__(self):
        return str(self.taxonID) + '\t' + str(self.nameID) + '\t' + self.status + '\t' + self.remarks + '\n'

    def __repr__(self):
        return str(self.taxonID) + '\t' + str(self.nameID) + '\t' + self.status + '\t' + self.remarks + '\n'
