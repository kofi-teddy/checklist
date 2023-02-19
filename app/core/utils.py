from fastapi import HTTPException, status
from typing import Any

# class CustomHTTPException(HTTPException):
#     def __init__(self, status_code: int=status.HTTP_400_BAD_REQUEST, detail: str=None, additional_data: dict=None):
#         super().__init__(status_code=status_code, detail=detail)
#         self.additional_data = additional_data


class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, detail: Any=None, headers: dict=None, additional_data: dict=None):
        self.additional_data = additional_data
        super().__init__(status_code=status_code, detail=detail, headers=headers)