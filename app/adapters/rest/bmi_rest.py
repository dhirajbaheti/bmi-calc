import logging
from fastapi import APIRouter, Response
from starlette import status
from app.config.logging import setup_logging
from app.core.models.bmi import BmiRequest, BmiResponse, PersonBmiResult, BmiAnalysis
from app.core.services.bmi_service import calculate_bmi, get_bmi_details, add_record_to_memory, Storage

router = APIRouter()

setup_logging()
logger = logging.getLogger(__name__)
storage = Storage()


@router.post(
    "/calculate_bmi", response_model=BmiResponse, status_code=status.HTTP_200_OK
)
def bmi(request: BmiRequest):
    logger.info(f"Request:- Gender:{request.gender}, Height:{request.height}, Weight:{request.weight}")

    try:
        if request.gender not in ('M', 'F'):
            raise Exception(f'Invalid gender specified {request.gender}. Valid values - M/F.')

        bmi_index = calculate_bmi(height=request.height, weight=request.weight)
        category, risk = get_bmi_details(bmi_index)
        bmi_result = PersonBmiResult(bmi=bmi_index, category=category, risk=risk)
        add_record_to_memory(storage, request, bmi_result)
        logger.info(f'BMI is "{bmi_index}" and person is "{category}" and has "{risk}".')
        return BmiResponse(bmi_result=bmi_result)
    except Exception as message:
        return BmiResponse(error=str(message))


@router.get(
    "/get_bmi_statistics", response_model=BmiAnalysis, status_code=status.HTTP_200_OK
)
def bmi(): return storage.show()
