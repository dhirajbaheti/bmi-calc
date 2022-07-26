from app.core.services.bmi_service import calculate_bmi, get_bmi_details


def test_calculate_bmi():
    bmi_index = calculate_bmi(height=183, weight=98)
    assert bmi_index == 29.3


def test_bmi_details():
    bmi_index = calculate_bmi(height=183, weight=98)
    category, risk = get_bmi_details(bmi_index)
    assert category == 'Overweight' and risk == 'Enhanced risk'