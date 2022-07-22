from api.services.base_service import Service
from api.models import Category


class CategoryService(Service):
    def __init__(self):
        super().__init__(Category)