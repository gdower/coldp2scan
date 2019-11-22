
class VernacularNameCOLDP:

    def __init__(self,
                 taxonID,
                 name,
                 transliteration='',
                 language='',
                 country='',
                 lifeStage='',
                 sex='',
                 referenceID=''):
        self.taxonID = taxonID
        self.name = name
        self.transliteration = transliteration
        self.language = language
        self.country = country
        self.lifeStage = lifeStage
        self.sex = sex
        self.referenceID = referenceID

    def __str__(self):
        return str(self.taxonID) + '\t' + self.name + '\t' + self.transliteration + '\t' + self.language + '\t' + \
               self.country + '\t' + self.lifeStage + '\t' + self.sex + '\t' + str(self.referenceID) + '\n'

    def __repr__(self):
        return str(self.taxonID) + '\t' + self.name + '\t' + self.transliteration + '\t' + self.language + '\t' + \
               self.country + '\t' + self.lifeStage + '\t' + self.sex + '\t' + str(self.referenceID) + '\n'
