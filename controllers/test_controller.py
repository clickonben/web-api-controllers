from fastapi import FastAPI

from controllers import BaseController


class TestController(BaseController):
    route_id = 'test'

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    @BaseController.get(route_id, '/')
    async def index(self) -> str:
        return 'Hello World!'

    @BaseController.get(route_id, '/test')
    async def test(self) -> str:
        return 'This is a test!'

    @BaseController.get(route_id, '/test2')
    async def test2(self) -> str:
        return 'This is another test!'

    def _get_route_id(self) -> str:
        return self.route_id
