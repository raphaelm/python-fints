import mt940
import re
from .models import Holding
from datetime import datetime


def mt940_to_array(data):
    data = data.replace("@@", "\r\n")
    data = data.replace("-0000", "+0000")
    transactions = mt940.models.Transactions()
    return transactions.parse(data)


def print_segments(message):
    segments = str(message).split("'")
    for idx, seg in enumerate(segments):
        print(u"{}: {}".format(idx, seg.encode('utf-8')))


def fints_escape(content):
    """
    Escape strings

    Ref:  https://www.hbci-zka.de/dokumente/spezifikation_deutsch/fintsv3/FinTS_3.0_Formals_2017-05-11_final_version.pdf
    Section  H.1.1
    """
    return content.replace('?', '??').replace('+', '?+').replace(':', '?:').replace("'", "?'")


def fints_unescape(content):
    return content.replace('??', '?').replace("?'", "'").replace('?+', '+').replace('?:', ':')


def split_for_data_groups(seg):
    return re.split('\+(?<!\?\+)', seg)


def split_for_data_elements(deg):
    return re.split(':(?<!\?:)', deg)


class MT535_Miniparser:
    re_identification = re.compile(r"^:35B:ISIN\s(.*)\|(.*)\|(.*)$")
    re_marketprice = re.compile(r"^:90B::MRKT\/\/ACTU\/([A-Z]{3})(\d*),{1}(\d*)$")
    re_pricedate = re.compile(r"^:98A::PRIC\/\/(\d*)$")
    re_pieces = re.compile(r"^:93B::AGGR\/\/UNIT\/(\d*),(\d*)$")
    re_totalvalue = re.compile(r"^:19A::HOLD\/\/([A-Z]{3})(\d*),{1}(\d*)$")

    def parse(self, lines):
        retval = []
        # First: Collapse multiline clauses into one clause
        clauses = self.collapse_multilines(lines)
        # Second: Scan sequence of clauses for financial instrument
        # sections
        finsegs = self.grab_financial_instrument_segments(clauses)
        # Third: Extract financial instrument data
        for finseg in finsegs:
            isin, name, market_price, price_symbol, price_date, pieces = (None,)*6
            for clause in finseg:
                # identification of instrument
                # e.g. ':35B:ISIN LU0635178014|/DE/ETF127|COMS.-MSCI EM.M.T.U.ETF I'
                m = self.re_identification.match(clause)
                if m:
                    isin = m.group(1)
                    name = m.group(3)
                # current market price
                # e.g. ':90B::MRKT//ACTU/EUR38,82'
                m = self.re_marketprice.match(clause)
                if m:
                    price_symbol = m.group(1)
                    market_price = float(m.group(2) + "." + m.group(3))
                # date of market price
                # e.g. ':98A::PRIC//20170428'
                m = self.re_pricedate.match(clause)
                if m:
                    price_date = datetime.strptime(m.group(1), "%Y%m%d").date()
                # number of pieces
                # e.g. ':93B::AGGR//UNIT/16,8211'
                m = self.re_pieces.match(clause)
                if m:
                    pieces = float(m.group(1) + "." + m.group(2))
                # total value of holding
                # e.g. ':19A::HOLD//EUR970,17'
                m = self.re_totalvalue.match(clause)
                if m:
                    total_value = float(m.group(2) + "." + m.group(3))
            # processed all clauses
            retval.append(
                Holding(
                    ISIN=isin, name=name, market_value=market_price,
                    value_symbol=price_symbol, valuation_date=price_date,
                    pieces=pieces, total_value=total_value))
        return retval

    def collapse_multilines(self, lines):
        clauses = []
        prevline = ""
        for line in lines:
            if line.startswith(":"):
                if prevline != "":
                    clauses.append(prevline)
                prevline = line
            elif line.startswith("-"):
                # last line
                clauses.append(prevline)
                clauses.append(line)
            else:
                prevline += "|{}".format(line)
        return clauses

    def grab_financial_instrument_segments(self, clauses):
        retval = []
        stack = []
        within_financial_instrument = False
        for clause in clauses:
            if clause.startswith(":16R:FIN"):
                # start of financial instrument
                within_financial_instrument = True
            elif clause.startswith(":16S:FIN"):
                # end of financial instrument - move stack over to
                # return value
                retval.append(stack)
                stack = []
                within_financial_instrument = False
            else:
                if within_financial_instrument:
                    stack.append(clause)
        return retval
