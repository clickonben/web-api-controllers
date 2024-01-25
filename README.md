# FastAPI Controllers

## Description
API controller framework for FastAPI

## Example
```python
from fastapi import FastAPI

class TestController(APIController):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    @Get('/')
    async def get(self) -> dict:
        return {"method": "GET", "path": "/"}

    @Get('/{arg}')
    async def get_with_arg(self, arg) -> dict:
        return {"method": "GET", "path": "/", "arg": arg}

    @Post('/')
    async def post(self) -> dict:
        return {"method": "POST", "path": "/"}

    @Post('/{arg}')
    async def post_with_arg(self, arg) -> dict:
        return {"method": "POST", "path": "/", "arg": arg}

app = FastAPI()
test_controller = TestController(app)
```