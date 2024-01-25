from fastapi import FastAPI
from controllers import TestController

app = FastAPI()
test_controller = TestController(app)
