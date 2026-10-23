import calendar
import datetime
from collections import namedtuple

SEPAAccount = namedtuple('SEPAAccount', 'iban bic accountnumber subaccount blz')

Saldo = namedtuple('Saldo', 'account date value currency')

Holding = namedtuple('Holding',
                     'ISIN name market_value value_symbol valuation_date pieces total_value acquisitionprice')

Amount = namedtuple('Amount', 'amount currency')

Transaction = namedtuple('Transaction', 'data')

SEPATransferPayment = namedtuple('SEPATransferPayment', 'recipient_name iban bic amount reason endtoend_id')


class VirtualDate(namedtuple('VirtualDate', 'year month day')):
    """Virtual date (FinTS format ``vdat``): Like a date, but every month may have 31 days,
    e.g. 2025-04-31 as execution date of a standing order."""
    __slots__ = ()

    @classmethod
    def from_date(cls, date: datetime.date):
        return cls(date.year, date.month, date.day)

    def to_date(self) -> datetime.date:
        """Convert to a ``datetime.date``. Days beyond the end of the month are moved to the last day of the month."""
        last_day = calendar.monthrange(self.year, self.month)[1]
        return datetime.date(self.year, self.month, min(self.day, last_day))

    def __str__(self):
        return "{:04d}-{:02d}-{:02d}".format(*self)
