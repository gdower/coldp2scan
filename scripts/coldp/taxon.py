
class TaxonCOLDP:

    ID = ''
    parentID = ''
    nameID = ''
    provisional = False
    accordingTo = ''
    accordingToID = ''
    accordingToDate = ''
    referenceID = ''
    extinct = ''
    temporalRangeStart = ''
    temporalRangeEnd = ''
    lifezone = ''
    link = ''
    remarks = ''

    def __init__(self,
                 ID,
                 parentID,
                 nameID,
                 provisional,
                 accordingTo,
                 accordingToID,
                 accordingToDate,
                 referenceID,
                 extinct,
                 temporalRangeStart,
                 temporalRangeEnd,
                 lifezone,
                 link,
                 remarks):

        self.ID = ID
        self.parentID = parentID
        self.nameID = nameID
        self.provisional = provisional
        self.accordingTo = accordingTo
        self.accordingToID = accordingToID
        self.accordingToDate = accordingToDate
        self.referenceID = referenceID
        self.extinct = extinct
        self.temporalRangeStart = temporalRangeStart
        self.temporalRangeEnd = temporalRangeEnd
        self.lifezone = lifezone
        self.link = link
        self.remarks = remarks

    def __str__(self):
        return str(self.ID)  + '\t' + str(self.parentID) + '\t' + str(self.nameID) + '\t' + \
               str(self.provisional) + '\t' + str(self.accordingTo) + '\t' + str(self.accordingToID) + '\t' + \
               str(self.accordingToDate) + '\t' + str(self.referenceID) + '\t' + str(self.extinct) + '\t' + \
               str(self.temporalRangeStart) + '\t' + str(self.temporalRangeEnd) + '\t' + self.lifezone + '\t' + self.link + '\t' + self.remarks + '\n'

    def __repr__(self):
        return str(self.ID)  + '\t' + str(self.parentID) + '\t' + str(self.nameID) + '\t' + \
               str(self.provisional) + '\t' + str(self.accordingTo) + '\t' + str(self.accordingToID) + '\t' + \
               str(self.accordingToDate) + '\t' + str(self.referenceID) + '\t' + str(self.extinct) + '\t' + \
               str(self.temporalRangeStart) + '\t' + str(self.temporalRangeEnd) + '\t' + self.lifezone + '\t' + self.link + '\t' + self.remarks + '\n'
