

menu = [{'title': "Add wallet", 'url_name': 'add_wallet'},
        {'title': "Add a test card", 'url_name': 'add_test_card'},
        {'title': "About", 'url_name': 'about'},]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.remove(user_menu[0])
            user_menu.remove(user_menu[0])

        context['menu'] = user_menu
        return context
