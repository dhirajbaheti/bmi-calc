import logging
from app.config.logging import setup_logging
from typing import List
from app.core.models.bmi import BmiDetails, PersonBmiResult, BmiAnalysis

setup_logging()
logger = logging.getLogger(__name__)


class Storage:
    """the storage (in memory in this case)"""
    def __init__(self) -> None:
        self.storage_list: List[BmiDetails] = []

    def add(self, item: BmiDetails) -> None:
        self.storage_list.append(item)

    def show(self) -> BmiAnalysis:
        """ Displays the statistics of the bmi. """
        analysis = BmiAnalysis()
        analysis.number_of_records = len(self.storage_list)
        analysis.results = []
        analysis.male = 0
        analysis.female = 0
        analysis.category_count = {'Underweight': 0, 'Normal weight': 0, 'Overweight': 0,
                                   'Moderately obese': 0, 'Severely obese': 0, 'Very severely obese': 0}
        for item in self.storage_list:
            if item.gender.upper() == 'M':
                analysis.male += 1
            elif item.gender.upper() == 'F':
                analysis.female += 1
            analysis.category_count[item.bmi_result.category] += 1
            analysis.results.append(item)

        return analysis


def calculate_bmi(height: int, weight: int) -> float:
    """
    Input: weight(Kg), height(cm)
    Output: bmi
    Formulae: BMI(kg/m2) = mass(kg) / height(m)2
    """

    return round(weight/((height/100)*(height/100)), 1)


def get_bmi_details(bmi):
    """
    Input: bmi
    Output: bmi_category & health_risk.
    """
    bmi_scale = [
        {'min': 0, 'max': 18.4, 'category': 'Underweight', 'risk': 'Malnutrition risk'},
        {'min': 18.5, 'max': 24.9, 'category': 'Normal weight', 'risk': 'Low risk'},
        {'min': 25, 'max': 29.9, 'category': 'Overweight', 'risk': 'Enhanced risk'},
        {'min': 30, 'max': 34.9, 'category': 'Moderately obese', 'risk': 'Medium risk'},
        {'min': 35, 'max': 39.9, 'category': 'Severely obese', 'risk': 'High risk'},
        {'min': 40, 'max': 99, 'category': 'Very severely obese', 'risk': 'above Very high risk'}
    ]

    if bmi < 0 or bmi > 99:
        raise Exception(f'Incorrect BMI value: {bmi}')

    for scale in bmi_scale:
        if scale['min'] <= bmi <= scale['max']:
            return scale['category'], scale['risk']


def add_record_to_memory(storage, request, bmi_result):
    """Add the person's bmi details to the memory. """
    bmi_details = BmiDetails()
    bmi_details.gender = request.gender
    bmi_details.height = request.height
    bmi_details.weight = request.weight
    bmi_details.bmi_result = bmi_result

    storage.add(bmi_details)
    logger.info(f"Record has been added to database!")
