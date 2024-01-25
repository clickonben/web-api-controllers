from fastapi import FastAPI
from routing import Get, Post, Put, Delete, Patch
from controllers import BaseController


class TestController(BaseController):

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

    @Put('/')
    async def put(self) -> dict:
        return {"method": "PUT", "path": "/"}

    @Put('/{arg}')
    async def put_with_arg(self, arg) -> dict:
        return {"method": "PUT", "path": "/", "arg": arg}

    @Delete('/')
    async def delete(self) -> dict:
        return {"method": "DELETE", "path": "/"}

    @Delete('/{arg}')
    async def delete_with_arg(self, arg) -> dict:
        return {"method": "DELETE", "path": "/", "arg": arg}

    @Patch('/')
    async def patch(self) -> dict:
        return {"method": "PATCH", "path": "/"}

    @Patch('/{arg}')
    async def patch_with_arg(self, arg) -> dict:
        return {"method": "PATCH", "path": "/", "arg": arg}

