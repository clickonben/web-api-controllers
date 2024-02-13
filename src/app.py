from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from src.webapicontrollers import APIController, Get, Post, Patch, Delete, Put, RoutePrefix

import logging

# Basic configuration for logging
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@RoutePrefix('/test')
class TestController(APIController):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app, debug_mode=True, cors_origins=['*'])    
    
    @Get('/')
    async def get(self) -> dict:
        return {"method": "GET", "path": "/"}    
        
    
    # @Get('/400')
    # async def get_bad_request(self) -> dict:
    #     raise HTTPException(status_code=400, detail="Bad Request")
    
    # @Get('/401')
    # async def get_not_authorized(self) -> dict:
    #     raise HTTPException(status_code=401, detail="Not Authorized")
    
    # @Get('/403')
    # async def get_forbidden(self) -> dict:
    #     raise HTTPException(status_code=403, detail="Forbidden")
    
    # @Get('/404')
    # async def get_not_found(self) -> dict:
    #     raise HTTPException(status_code=404, detail="Not Found")
    
    # @Get('/405')
    # async def get_method_not_allowed(self) -> dict:
    #     raise HTTPException(status_code=405, detail="Method Not Allowed")
    
    # @Get('/500')
    # async def get_internal_server_error(self) -> dict:
    #     raise HTTPException(status_code=500, detail="Internal Server Error")
    
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
    
    @Patch('/')
    async def patch(self) -> dict:
        return {"method": "PATCH", "path": "/"}
    
    @Patch('/{arg}')
    async def patch_with_arg(self, arg) -> dict:
        return {"method": "PATCH", "path": "/", "arg": arg}
    
    @Delete('/')
    async def delete(self) -> dict:
        return {"method": "DELETE", "path": "/"}
    
    @Delete('/{arg}')
    async def delete_with_arg(self, arg) -> dict:
        return {"method": "DELETE", "path": "/", "arg": arg}
    
    def bad_request(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().bad_request(request, exc)
    
    def not_authorized(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().not_authorized(request, exc)
    
    def forbidden(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().forbidden(request, exc)
    
    def not_found(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().not_found(request, exc)
    
    def method_not_allowed(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().method_not_allowed(request, exc)
    
    def internal_server_error(self, request: Request, exc: HTTPException) -> JSONResponse:
        # Custom handling code
        return super().internal_server_error(request, exc)


app = FastAPI()

TestController(app)