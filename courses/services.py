from config.settings import stripe


def get_payment(course, amount):
    product = stripe.Product.create(name=course.title)

    price = stripe.Price.create(
      unit_amount=amount,
      currency='rub',
      product=product.id,
    )

    session = stripe.checkout.Session.create(
      # client_reference_id=course.pk,
      success_url=f"http://127.0.0.1:8000/lesson/check_pay/{course.pk}",
      line_items=[
        {
          "price": price.id,
          "quantity": 1,
        },
      ],
      mode="payment",
    )

    return session


def is_paid(session):

    if session.payment_status == 'paid':
        return True
    return False
