from typing import Optional, List
from pydantic import Field, BaseModel


class PersonBmiResult(BaseModel):
    bmi: Optional[float] = Field(example=23.2)
    category: Optional[str] = Field(example="Normal weight")
    risk: Optional[str] = Field(example="Low risk")


class BmiDetails(BaseModel):
    gender: Optional[str]
    height: Optional[int]
    weight: Optional[int]
    bmi_result: Optional[PersonBmiResult]


class BmiAnalysis(BaseModel):
    number_of_records: Optional[int]
    male: Optional[float]
    female: Optional[float]
    category_count: Optional[dict]
    results: Optional[List[BmiDetails]]


class BmiRequest(BaseModel):
    gender: str = Field(example="M")
    height: int = Field(example=175)
    weight: int = Field(example=75)


class BmiResponse(BaseModel):
    bmi_result: Optional[PersonBmiResult] = Field()
    error: Optional[str] = Field(example="Invalid value")