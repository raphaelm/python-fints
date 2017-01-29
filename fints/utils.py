import mt940


def mt940_to_array(data):
    data = data.replace("@@", "\r\n")
    data = data.replace("-0000", "+0000")
    transactions = mt940.models.Transactions()
    return transactions.parse(data)
