from django.db import transaction
from django.db.models import F
from app.models import App
from wallet.models import Wallet
from .models import Purchase
from rest_framework.exceptions import ValidationError


def create_purchase(user, app_id):
    with transaction.atomic():
        # Lock the wallet record to prevent concurrent modifications
        wallet = Wallet.objects.select_for_update().get(user=user)

        # Check if the wallet has enough balance
        app = App.objects.get(id=app_id)
        if wallet.balance < app.price:
            raise ValidationError("Insufficient balance.")

        wallet.balance = F('balance') - app.price
        wallet.save()

        purchase = Purchase.objects.create(user=user, app=app, price=app.price)

        return purchase
