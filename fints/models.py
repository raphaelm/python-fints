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


class TANMethod(DataClass):
    pass


class TANMethod5(TANMethod):
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #5
    version = 5
    args = ['security_feature', 'tan_process', 'tech_id', 'zka_id', 'zka_version', 'name', 'max_length_input',
            'allowed_format', 'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists',
            'multiple_tans_allowed', 'tan_time_dialog_association', 'tan_list_number_required', 'cancel_allowed',
            'sms_charge_account_required', 'principal_account_required', 'challenge_class_required',
            'challenge_value_required', 'initialization_mode', 'description_required', 'supported_media_number']


class TANMethod6(TANMethod):
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #6
    version = 6
    args = ['security_feature', 'tan_process', 'tech_id', 'zka_id', 'zka_version', 'name', 'max_length_input',
            'allowed_format', 'text_returnvalue', 'max_length_returnvalue', 'multiple_tans_allowed',
            'tan_time_dialog_association', 'cancel_allowed', 'sms_charge_account_required',
            'principal_account_required',
            'challenge_class_required', 'challenge_structured', 'initialization_mode', 'description_required',
            'hhd_uc_required', 'supported_media_number']


class TANChallenge(DataClass):
    def __init__(self, dialog, *args, **kwargs):
        self.dialog = dialog
        super().__init__(*args, **kwargs)


class TANChallenge3(TANChallenge):
    version = 3
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge4(TANChallenge):
    version = 4
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge5(TANChallenge):
    version = 5
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'tan_list_number', 'ben', 'medium_description']


class TANChallenge6(TANChallenge):
    version = 6
    args = ['tan_process', 'request_hash', 'reference', 'challenge', 'challenge_hhd_uc', 'challenge_datetime',
            'medium_description']