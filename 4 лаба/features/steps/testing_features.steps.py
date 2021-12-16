from behave import *
from TDD_Test.TDD_test import *

@given("Product_Builder")
def first_step(context):
    context.a = Product_Builder_Test()

@when("test_ATAK_builder return OK")
def test_ATAK_builder(context):
    context.a.test_ATAK_builder()

@when("test_Magnit_builder return OK")
def test_Magnit_builder(context):
    context.a.test_Magnit_builder()

@then("Good job")
def last_step(context):
    pass

