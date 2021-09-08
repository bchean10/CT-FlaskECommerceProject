# from . import bp as api
# from .models import Item, Category
# from app.blueprints.auth.auth import token_auth
# from flask import request, make_response, g
# import stripe
# import os

# stripe.api_key = 'sk_test_51JSVUqLkVcxO568O9o2s5dD4Z63cIUxSIlKzpULmQUxHKut49KkHSQPOdvsuNgIa79OHxjGqTRuWybIrlLVJXgbl00MtaJFEtZ'

# YOUR_DOMAIN = 'http://localhost:3000'
# @api.route('/create-checkout-session', methods=['POST'])
# def create_checkout_session():
#     cart=request.get_json().get('cart')
#     line_items=[{'name':cart[item_key]['name'],
#                  'amount':int(round(float(cart[item_key]['price']),2)*100),
#                  'currency':'USD',
#                  'quantity':cart[item_key]['quantity']} for item_key in cart.keys()]
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             billing_address_collection='auto',

#             line_items=line_items,
#             payment_method_types=[
#               'card',
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/checkoutSuccess',
#             cancel_url=YOUR_DOMAIN + '/cart',
#         )
#     except Exception as e:
#         return str(e)
#     return {'url':checkout_session.url}


# @api.get('/category')
# @token_auth.login_required()
# def get_category():
#     cats = Category.query.all()
#     cats_dicts = [cat.to_dict() for cat in cats]
#     return make_response({"categories":cats_dicts},200)


# @api.post('/category')
# @token_auth.login_required()
# def post_category():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     cat_name = request.get_json().get('name')
#     cat = Category(name = cat_name)
#     cat.save()
#     return make_response(f"category {cat.id} with name {cat.name} created",200)

# @api.put('/category')
# @token_auth.login_required()
# def patch_category():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     cat_name = request.get_json().get('name')
#     cat_id = request.get_json().get('id')
#     if not cat_name or not cat_id:
#         return make_response("Invalid Payload",400)
#     cat = Category.query.get(cat_id)
#     if cat is None:
#         return make_response("Invalid category id", 400)
#     cat.name = cat_name
#     cat.save()
#     return make_response(f"category {cat.id} has a new name {cat.name}",200)


# @api.delete('/category')
# @token_auth.login_required()
# def delete_category():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     cat_id = request.get_json().get('id')
#     if not cat_id:
#         return make_response("Invalid Payload",400)
#     cat = Category.query.get(cat_id)
#     if cat is None:
#         return make_response("Invalid category id", 400)    
#     cat_id = cat.id
#     cat.delete()
#     return make_response(f"Category {cat_id} has been deleted", 200)



# @api.get("/item")
# @token_auth.login_required()
# def get_item():
#     id = request.args.get('id')
#     if not id:
#         return make_response("Invalid Payload",400)
#     item = Item.query.get(id)
#     if item is None:
#         return make_response("Invalid item id", 400)
#     return make_response(item.to_dict(),200)


# @api.get("/all_items")
# @token_auth.login_required()
# def get_all_items():
#     all_items = Item.query.all()
#     items = [item.to_dict() for item in all_items]
#     return make_response({"items":items},200)


# @api.get("/items_by_category_id")
# @token_auth.login_required()
# def items_by_category_id():
#     id = request.args.get('id') 
#     if not id:
#         return make_response("Invalid Payload",400)
#     all_items = Item.query.filter_by(category_id=id).all()
#     items = [item.to_dict() for item in all_items]
#     return make_response({"items":items},200)


# @api.post("/item")
# @token_auth.login_required()
# def post_item():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     item_dict = request.get_json()
#     print(item_dict)
#     if not all(key in item_dict for key in ('name','description','price','img','category_id')):
#         return make_response("Invalid Payload",400)
#     print("here1")
#     item = Item(**item_dict)
#     print("here2")
#     item.save()
#     return make_response(f"Item {item.name} was created with the id {item.id}",201)


# @api.put("/item")
# @token_auth.login_required()
# def patch_item():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     item_dict = request.get_json()
#     print(item_dict)
#     if not item_dict.get('id'):
#         return make_response("Invalid Payload",400)
#     item = Item.query.get(item_dict['id'])
#     item.from_dict(item_dict)
#     item.save()
#     return make_response(f'Item {item.id} was edited', 200)


# @api.delete("/item")
# @token_auth.login_required()
# def delete_item():
#     if not g.current_user.is_admin:
#         return make_response("You Are not Admin",403)
#     id = request.get_json().get('id')
#     if not id:
#         return make_response("Invalid Payload",400)
#     item_to_delete = Item.query.get(id)
#     if item_to_delete is None:
#         return make_response("Invalid item id", 400)
#     item_to_delete.delete()
#     return make_response(f"Item id {id} has been deleted")

