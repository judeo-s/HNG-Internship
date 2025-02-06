from fastapi import FastAPI, Query, status, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json
from utils import (
    is_even,
    is_odd,
    is_armstrong,
    is_prime, is_perfect,
    digit_sum,
    get_fun_fact)
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
async def classify_number(number: Optional[str] = Query(None, description="Number to classify")):
    """
    Classifies a given number by evaluating its mathematical properties 
    and provides a fun fact.

    This endpoint accepts an optional number as a query parameter and 
    checks if the number is Armstrong, odd, even, prime, and perfect. 
    It also calculates the sum of its digits and fetches a fun fact 
    about the number.

    Args:
        number (Optional[str]): The number to classify. If not provided, 
        returns an error response.

    Returns:
        JSON response containing:
            - number (str): The input number.
            - is_prime (bool): Whether the number is prime.
            - is_perfect (bool): Whether the number is perfect.
            - properties (List[str]): List of properties the number satisfies 
              (e.g., "armstrong", "odd", "even").
            - digit_sum (int): The sum of the digits of the number.
            - fun_fact (str): A fun fact about the number.
            - error (bool): True if there was an error, False otherwise.
    """
    if number is None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=json.dumps({"number": "alphabet", "error": True}), media_type="application/json")
    try:
        num = int(number)
    except ValueError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST,
                        content=json.dumps({"number": "alphabet", "error": True}), media_type="application/json")

    armstrong = is_armstrong(num)
    odd = is_odd(num)
    even = is_even(num)
    properties: List[str] = []

    if armstrong and odd:
        properties = ["armstrong", "odd"]
    elif armstrong and even:
        properties = ["armstrong", "even"]
    elif odd:
        properties = ["odd"]
    elif even:
        properties = ["even"]

    try:
        fun_fact = await get_fun_fact(num)
    except Exception as e:
        fun_fact = f"Error fetching fun fact: {e}"

    return {
        "number": number,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact,
    }