
class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the session key does not exist, create a new session key and save it to the session dictionary
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product):
        # Get the product id
        product_id = str(product.id)

        # Logic - If the product id is not in the cart, add it
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        # Save the session
        self.session.modified = True

    def __len__(self):
        return len(self.cart)