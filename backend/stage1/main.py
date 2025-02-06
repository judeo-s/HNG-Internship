from fastapi import FastAPI, Query, status, Response
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Any
from utils import is_armstrong, is_prime, is_perfect, digit_sum, get_fun_fact
"""
Number Facts API that provides interesting mathematical properties about a given number,
along with a fun fact
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number")
async def classify_number(number: Any = Query(...)) -> Any:
    """
    Classify a given number, given as a query parameter, into its properties such as
    whether it is prime, perfect, armstrong, odd or even, and provides a fun fact
    about the number.

    Args:
        number: The number whose properties are to be classified

    Returns:
        A JSON response with the following keys:
        - number: The given number
        - is_prime: Whether the number is prime
        - is_perfect: Whether the number is perfect
        - properties: A list of properties the number has
        - digit_sum: The sum of the digits of the number
        - fun_fact: A fun fact about the number

    Raises:
        Bad Request (400) if the number given is not an integer
    """
    try:
        number = int(number)
        armstrong = is_armstrong(number)
        properties = []
        if armstrong:
            properties.append("armstrong")
        properties.append("odd" if number % 2 else "even")

        fact = await get_fun_fact(number)

        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": fact
        }
    except Exception as e:
        error_message = {"number": "alphabet", "error": True}
        return Response(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=json.dumps(error_message),
            media_type="application/json"
        )