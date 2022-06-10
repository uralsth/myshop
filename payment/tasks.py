from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from io import BytesIO
from orders.models import Order
import weasyprint

@shared_task
def payment_completed(order_id):
    """
    Task to send an email notification when an order is succesfully created.
    """
    order = Order.objects.get(id=order_id)

    # create invoice email
    subject = f'My shop - EE Invoice no. {order.id}'
    message = 'Please, find atteached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com',[order.email])

    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO
    stylesheets = [weasyprint.CSS(settings.STATC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets) 

    # attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    # send e-mail
    email.send()
