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


class TANMethod1(TANMethod):
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_delayed_allowed:
    """
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #1
    version = 1
    args = ['security_feature', 'tan_process', 'tech_id', 'name', 'max_length_input', 'allowed_format',
            'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists', 'multiple_tans_allowed',
            'tan_time_delayed_allowed']


class TANMethod2(TANMethod):
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_dialog_association:
    :param tan_list_number_required:
    :param cancel_allowed:
    :param challenge_class_required:
    :param challenge_value_required:
    """
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #2
    version = 2
    args = ['security_feature', 'tan_process', 'tech_id', 'name', 'max_length_input', 'allowed_format',
            'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists', 'multiple_tans_allowed',
            'tan_time_dialog_association', 'tan_list_number_required', 'cancel_allowed', 'challenge_class_required',
            'challenge_value_required']



class TANMethod3(TANMethod):
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_dialog_association:
    :param tan_list_number_required:
    :param cancel_allowed:
    :param challenge_class_required:
    :param challenge_value_required:
    :param initialization_mode:
    :param description_required:
    :param supported_media_number:
    """
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #3
    version = 3
    args = ['security_feature', 'tan_process', 'tech_id', 'name', 'max_length_input', 'allowed_format',
            'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists', 'multiple_tans_allowed',
            'tan_time_dialog_association', 'tan_list_number_required', 'cancel_allowed', 'challenge_class_required',
            'challenge_value_required', 'initialization_mode', 'description_required', 'supported_media_number']


class TANMethod4(TANMethod):
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param zka_id:
    :param zka_version:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_dialog_association:
    :param tan_list_number_required:
    :param cancel_allowed:
    :param sms_charge_account_required:
    :param challenge_class_required:
    :param challenge_value_required:
    :param challenge_structured
    :param initialization_mode:
    :param description_required:
    :param supported_media_number:
    """
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #4
    version = 4
    args = ['security_feature', 'tan_process', 'tech_id', 'zka_id', 'zka_version', 'name', 'max_length_input',
            'allowed_format', 'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists',
            'multiple_tans_allowed', 'tan_time_dialog_association', 'tan_list_number_required', 'cancel_allowed',
            'sms_charge_account_required', 'challenge_class_required', 'challenge_value_required',
            'challenge_structured', 'initialization_mode', 'description_required', 'supported_media_number']



class TANMethod5(TANMethod):
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param zka_id:
    :param zka_version:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_dialog_association:
    :param tan_list_number_required:
    :param cancel_allowed:
    :param sms_charge_account_required:
    :param principal_account_required:
    :param challenge_class_required:
    :param challenge_value_required:
    :param initialization_mode:
    :param description_required:
    :param supported_media_number:
    """
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #5
    version = 5
    args = ['security_feature', 'tan_process', 'tech_id', 'zka_id', 'zka_version', 'name', 'max_length_input',
            'allowed_format', 'text_returnvalue', 'max_length_returnvalue', 'number_of_supported_lists',
            'multiple_tans_allowed', 'tan_time_dialog_association', 'tan_list_number_required', 'cancel_allowed',
            'sms_charge_account_required', 'principal_account_required', 'challenge_class_required',
            'challenge_value_required', 'initialization_mode', 'description_required', 'supported_media_number']


class TANMethod6(TANMethod):
    # Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #6
    """
    :param security_feature:
    :param tan_process:
    :param tech_id:
    :param zka_id:
    :param zka_version:
    :param name:
    :param max_length_input:
    :param allowed_format:
    :param text_returnvalue:
    :param max_length_returnvalue:
    :param number_of_supported_lists:
    :param multiple_tans_allowed:
    :param tan_time_dialog_association:
    :param cancel_allowed:
    :param sms_charge_account_required:
    :param principal_account_required:
    :param challenge_class_required:
    :param challenge_value_required:
    :param initialization_mode:
    :param description_required:
    :param hhd_uc_required:
    :param supported_media_number:
    """
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