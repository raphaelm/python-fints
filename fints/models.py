from collections import namedtuple

SEPAAccount = namedtuple('SEPAAccount', 'iban bic accountnumber subaccount blz')

Saldo = namedtuple('Saldo', 'account date value currency')

Holding = namedtuple('Holding',
                     'ISIN name market_value value_symbol valuation_date pieces total_value acquisitionprice')


class DataClass:
    def __init__(self, *args, **kwargs):
        for i, a in enumerate(args):
            setattr(self, self.args[i], a)
        for k, v in kwargs.items():
            if k in self.args:
                setattr(self, k, v)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{}={}'.format(k, repr(getattr(self, k, None))) for k in self.args])
        )



class TANChallenge(DataClass):
    def __init__(self, dialog, *args, **kwargs):
        self.dialog = dialog
        super().__init__(*args, **kwargs)


class TANChallenge3(TANChallenge):
    """
    :param tan_process:
    :param request_hash:
    :param reference:
    :param challenge:
    :param challenge_datetime:
    :param tan_list_number:
    :param ben:
    :param medium_description:
    """
    version = 3
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge4(TANChallenge):
    """
    :param tan_process:
    :param request_hash:
    :param reference:
    :param challenge:
    :param challenge_hhd_uc:
    :param challenge_datetime:
    :param tan_list_number:
    :param ben:
    :param medium_description:
    """
    version = 4
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge5(TANChallenge):
    """
    :param tan_process:
    :param request_hash:
    :param reference:
    :param challenge:
    :param challenge_hhd_uc:
    :param challenge_datetime:
    :param tan_list_number:
    :param ben:
    :param medium_description:
    """
    version = 5
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge6(TANChallenge):
    """
    :param tan_process:
    :param request_hash:
    :param reference:
    :param challenge:
    :param challenge_hhd_uc:
    :param challenge_datetime:
    :param medium_description:
    """
    version = 6
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'medium_description']