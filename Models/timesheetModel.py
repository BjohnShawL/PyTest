class Timesheet(object):
    def __init__(self, placementRef, tsStatus, startDate, endDate, numericID):
        self.placementRef = placementRef
        self.tsStatus = tsStatus
        self.startDate = startDate
        self.endDate = endDate
        self.numericID = numericID
