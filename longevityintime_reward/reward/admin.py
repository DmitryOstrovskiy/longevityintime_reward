from django.contrib import admin

from .models import Wallet, TestCard


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_address', 'wallet_balance',
                    'private_key', 'public_key', 'mnemonic_phrase')
    search_fields = ('user', 'wallet_address')
    empty_value_display = '-empty-'
    list_filter = ('user', 'wallet_address')


@admin.register(TestCard)
class TestCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'parameter', 'parameter_value',
                    'pub_date', 'author')
    search_fields = ('name', 'parameter', 'pub_date', 'author')
    empty_value_display = '-empty-'
    list_filter = ('name', 'parameter', 'pub_date', 'author')
