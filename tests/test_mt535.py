from fints.utils import MT535_Miniparser


def _mt535_holding(isin, name, pieces, total_value=None):
    lines = [
        ":16R:FIN",
        ":35B:ISIN {}|/DE/X1|{}".format(isin, name),
        ":90B::MRKT//ACTU/EUR10,00",
        ":98A::PRIC//20260101",
        ":93B::AGGR//UNIT/{},".format(pieces),
    ]
    if total_value is not None:
        lines.append(":19A::HOLD//EUR{}".format(total_value))
    lines.append(":16S:FIN")
    return lines


def test_mt535_holding_without_total_value_does_not_inherit_previous():
    lines = _mt535_holding("AA0000000001", "ONE", "5", "50,00")
    lines += _mt535_holding("AA0000000002", "TWO", "7")
    lines.append("-")

    first, second = MT535_Miniparser().parse(lines)

    assert first.total_value == 50.0
    assert second.total_value is None


def test_mt535_first_holding_without_total_value():
    lines = _mt535_holding("AA0000000003", "THREE", "1") + ["-"]

    (holding,) = MT535_Miniparser().parse(lines)

    assert holding.total_value is None
