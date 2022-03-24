from datetime import datetime


def add(a, b):
    if a == 50:
        return 1.2
    return a + b


def test_check_for_0_0():
    assert add(0, 0) == 0


def test_check_for_0_1():
    assert add(0, 1) == 1


def test_check_for_0_2():
    assert add(0, 2) == 2


def test_check_for_0_3():
    assert add(0, 3) == 3


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    year = pesel[0: 2]
    month = int(pesel[2:4])
    if month > 20 and month < 40:
        month -= 20
        year = int('20' + year)
    else:
        year = int("19" + year)
    day = int(pesel[4:6])
    birth_date = datetime(year , month, day)
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


import pytest


@pytest.mark.parametrize("pesel", [
    '73090992548', '71050733594', '98061671112',
    '89050561165', '03280284755', '98091228249',
    '55040542416', '69110628588', '69081682392', '50051834428'])
def test_check_if_ap_return_correct_pesel(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['pesel'] == pesel

@pytest.mark.parametrize("pesel", [
    '73090992548', '71050733594', '98061671112',
    '89050561165', '03280284755', '98091228249',
    '55040542416', '69110628588', '69081682392', '50051834428'])
def test_check_if_ap_pesel_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['valid']

@pytest.mark.parametrize("pesel", [
    '73091992548', '71051733594', '98062671112',
    '89051561165', '03281284755', '98092228249',
    '55041542416', '69111628588', '69082682392', '50051834421'])
def test_check_if_ap_pesel_not_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert not ret_val['valid']

@pytest.mark.parametrize("pesel", [
    '53052288159', '53051622437', '89030873619',
    '57070597635', '53091011954', '88051346278',
    '73080191519', '86061422111', '00251052632',
    '63042893539']
)
def test_check_if_ap_pesel_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['gender'] == 'male'

@pytest.mark.parametrize("pesel", [
    '95070465424', '70040154782', '69090323624',
    '75051858186', '84051035121', '85101891744',
    '04211589989', '75020382168', '53091828684', '48070687347']
)
def test_check_if_ap_pesel_valid(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['gender'] == 'female'



@pytest.mark.parametrize("pesel, bd", [
    ('73090992548', datetime(1973,9,9)),
    ('71050733594', datetime(1971,5,7)), ])
def test_check_if_ap_pesel_valid(pesel, bd):
    ret_val = analyze_pesel(pesel)
    assert ret_val['birth_date'] == bd
