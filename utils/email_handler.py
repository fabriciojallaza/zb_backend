from django.core.mail import send_mail
from core.models import User


def email_handler(product):
    """Send an email to admins if product is updated"""

    subject = 'Product Updated'
    message = f'Product {product.name} with SKU {product.sku}, has been updated.\n\nZB Team.'
    email_from = 'fabriciojallaza@gmail.com'
    recipient_list = [email for email in User.objects.all().values_list('email', flat=True).filter(is_staff=True)]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)

