# from . import bp as data
# from .models import Item, Category
# from flask import request, make_response, render_template

# @data.get('/category')
# @token_auth.login_required()
# def get_category():
#     cats = Category.query.all()
#     cats_dicts = [cat.to_dict() for cat in cats]
#     return make_response({"categories":cats_dicts}, 200)

# @data.post('/category')
# @token_auth.login_required()
# def post_category():
#     cat_name = request.get_json().get('name')
#     cat = Category(name = cat_name)
#     cat.save()
#     return make_response(f"category {cat.id} with name {cat.name} created", 200)

# @data.patch('/category')
# @token_auth.login_required()
# def patch_category():
#     cat_name = request.get_json().get('name')
#     cat_id = request.get_json().get('id')
#     if not cat_name or not cat_id:
#         return make_response("Invalid payload", 400)
#     cat = Category.query.get(cat_id)
#     if cat is None:
#         return make_response("Invalid category id", 400)
#     cat.name = cat_name
#     cat.save()
#     return make_response(f"category {cat.id} has a new name {cat.name}", 200)

# @data.delete('/category')
# @token_auth.login_required()
# def delete_category():
#     cat_id = request.get_json().get('id')
#     if not cat_id:
#         return make_response("Invalid payload", 400)
#     cat = Category.query.get(cat_id)
#     if cat is None:
#         return make_response("Invalid category id", 400)
#     cat_id = cat.id
#     cat.delete()
#     return make_response(f"Category {cat_id} has been deleted.", 200)


# @data.get('/item')
# @token_auth.login_required()
# def get_item():
#     id = request.get_json().get('id')
#     if not id:
#         return make_response("Invalid Payload", 400)
#     item = Item.query.get(id)
#     if item is None:
#         return make_response("Invalid item id", 400)
#     return make_response(item.to_dict(), 200)


# @data.get('all_item')
# @token_auth.login_required()
# def get_all_item():
#     all_items = Item.query.all()
#     items = [item.to_dict() for item in all_items]
#     return make_response({"items":items}, 200)


# @data.get('/items_by_category_id')
# @token_auth.login_required()
# def items_by_category_id():
#     id = request.get_json().get('id') 
#     if not id:
#         return make_response("Invalid Payload", 400)
#     all_items = Item.query.filter_by(category_id=id).all()
#     items = [item.to_dict() for item in all_items]
#     return make_response({"items":items}, 200)

# @data.post('/item')
# @token_auth.login_required()
# def post_item():
#     item_dict = request.get_json()
#     if not all(key in item_dict for key in ('name', 'description', 'price', 'img', 'category_id')):
#         return make_response("Invalid payload", 400)
#     item = Item(**item_dict)
#     item.save()
#     return make_response(f"Item {item.id} with name {item.name} created", 200)
    

# @data.patch('/item')
# @token_auth.login_required()
# def patch_item():
#     item_dict = request.get_json()
#     if not item_dict.get('id'):
#         return make_response("Invalid payload", 400)
#     item = Item.query.get(item_dict['id'])
#     item.from_dict(item_dict)
#     item.save()
#     return make_response(f"Item {item.id} was edited", 200)


# @data.delete('/item')
# @token_auth.login_required()
# def delete_item():
#     id = request.get_json().get('id')
#     if not id:
#         return make_response("Invalid Payload", 400)
#     item_to_delete = Item.query.get(id)
#     if item_to_delete is None:
#         return make_response("Invalid item id", 400)
#     item_to_delete.delete()
#     return make_response(f"Item id {id} has been deleted")