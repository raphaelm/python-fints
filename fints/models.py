from collections import namedtuple

SEPAAccount = namedtuple('SEPAAccount', 'iban bic accountnumber subaccount blz country_id')

Saldo = namedtuple('Saldo', 'account date value currency')

Holding = namedtuple('Holding',
                     'ISIN name market_value value_symbol valuation_date pieces total_value acquisitionprice')


class StatementOfHoldings:

    total_value = 0.0
    holdings = []
