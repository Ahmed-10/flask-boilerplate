from api.controllers.base_controller import Controller
from api.services.category import CategoryService


class CategoryController(Controller):
    def __init__(self):
        super().__init__(CategoryService)