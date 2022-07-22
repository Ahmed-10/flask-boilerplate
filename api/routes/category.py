from flask import Blueprint, request
from api.controllers.category import CategoryController

category_api = Blueprint('category_api', __name__, url_prefix='/categories')


@category_api.route('/')
def get_all_categories():
    return CategoryController().all()


@category_api.route('/<int:id>')
def get_category(id):
    return CategoryController().one(id)


@category_api.route('/', methods=['POST'])
def create_category():
    return CategoryController().create(request.json)


@category_api.route('/<int:id>', methods=['PUT'])
def update_category(id):
    return CategoryController().update(id, request.json)


@category_api.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    return CategoryController().del_one(id)