def timeDifference(fromDate, toDate):
    period = toDate - fromDate
    result = period.total_seconds()/(60*60*24*365)
    return result

