import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from behave import given, when, then

from calculator import calculate_total
from order_builder import OrderBuilder
from product import Product


@given('an order with 2 t-shirts at $250 and 1 cap at $150')
def step_impl(context):
    context.order = (
        OrderBuilder()
        .add_item(Product("t_shirt", price=250), quantity=2)
        .add_item(Product("cap", price=150), quantity=1)
        .build()
    )


@given('an order with 1 cap at $150')
def step_impl(context):
    context.order = OrderBuilder().add_item(Product("cap", price=150), quantity=1).build()


@when('I apply the coupon "{coupon}"')
def step_impl(context, coupon):
    context.total = calculate_total(context.order, coupon=coupon)


@when("I don't apply any coupon")
def step_impl(context):
    context.total = calculate_total(context.order)


@then('the total should be ${expected}')
def step_impl(context, expected):
    expected_total = float(expected)
    assert context.total == expected_total, f"expected {expected_total}, got {context.total}"
