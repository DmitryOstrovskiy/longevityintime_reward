from django.contrib import admin

from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet_address', 'wallet_balance',
                    'private_key', 'public_key', 'mnemonic_phrase')
    search_fields = ('user', 'wallet_address')
    empty_value_display = '-empty-'
    list_filter = ('user', 'wallet_address')
