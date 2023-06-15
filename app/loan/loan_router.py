from fastapi import APIRouter
from pydantic import BaseModel

from loan.expected_loan_check import calculate_score, calculate_loan

loan_router = APIRouter()


class RequestUserInfo(BaseModel):
    income: int
    private_loan_outstanding_amount: int
    outstanding_amount: int


@loan_router.post("/request-loan-amount")
async def receive_vue_data(request: RequestUserInfo):
    print("vue에서 자산 정보 받기!")
    total_score = calculate_score(request.income, request.private_loan_outstanding_amount, request.outstanding_amount)
    loan_amount = calculate_loan(total_score)

    return loan_amount