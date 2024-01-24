from enums import HTTPMethods
from fastapi import FastAPI


class BaseController:
    routes = {}

    def __init__(self,
                 app: FastAPI
                 ) -> None:
        self.app = app

    def _get_route_id(self):
        """Subclasses should override this method to return a unique identifier."""
        raise NotImplementedError("Subclasses must implement get_route_id method")

    def __register_routes(self):
        route_id = self._get_route_id()
        for (route_id, method), funcs in self.routes.get(route_id, []):
            for func, path in funcs:
                def route_handler(func=func, self=self, **kwargs):
                    return func(self, **kwargs)
                self.app.add_api_route(
                    path=f"/{route_id}{path}",
                    endpoint=route_handler,
                    methods=[method.value]
                )

    @classmethod
    def get(
            cls,
            route_id: str = None,
            path: str = ""
    ) -> callable:
        return cls.create_decorator(HTTPMethods.GET, route_id, path)

    @classmethod
    def create_decorator(cls,
                         method: HTTPMethods,
                         route_id: str = None,
                         path: str = ""
                         ) -> callable:
        def decorator(func):
            if route_id not in cls.routes:
                cls.routes[route_id] = []
            cls.routes[(route_id, method)].append((func, path))
            return func

        return decorator
