from collections import namedtuple

SEPAAccount = namedtuple('SEPAAccount', 'iban bic accountnumber subaccount blz')

Saldo = namedtuple('Saldo', 'account date value currency')

Holding = namedtuple('Holding',
                     'ISIN name market_value value_symbol valuation_date pieces total_value acquisitionprice')


# Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #5
TANMethod5 = namedtuple('TANMethod5', 'security_feature tan_process tech_id zka_id zka_version name max_length_input '
                                      'allowed_format text_returnvalue max_length_returnvalue '
                                      'number_of_supported_lists multiple_tans_allowed '
                                      'tan_time_dialog_association tan_list_number_required '
                                      'cancel_allowed sms_charge_account_required principal_account_required '
                                      'challenge_class_required challenge_value_required '
                                      'initialization_mode description_required supported_media_number')

# Source: PIN/TAN docs – Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #6
TANMethod6 = namedtuple('TANMethod6', 'security_feature tan_process tech_id zka_id zka_version name max_length_input '
                                      'allowed_format text_returnvalue max_length_returnvalue '
                                      'multiple_tans_allowed tan_time_dialog_association '
                                      'cancel_allowed sms_charge_account_required principal_account_required '
                                      'challenge_class_required challenge_structured '
                                      'initialization_mode description_required hhd_uc_required '
                                      'supported_media_number')
