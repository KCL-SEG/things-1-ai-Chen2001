from pydoc import describe
from django.test import TestCase

from django.core.exceptions import ValidationError
from .models import Thing 
# Create your tests here.
class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing=Thing.objects.create(
            name='apple',
            description="red and sweet",
            quantity=100
        )
    
    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except (ValidationError):
            self.fail("Test thing should be valid")
    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
    def _test_quantity_cannot_be_less_than_0(self):
        self.thing.quantity<0
        self._assert_thing_is_invalid()
    def _test_quantity_cannot_be_larger_than_100(self):
        self.thing.quantity>100
        self._assert_thing_is_invalid()
    
    def _test_quantity_can_be_equal_to_0(self):
        self.thing.quantity=0
        self._assert_thing_is_valid()
    def _test_quantity_can_be_equal_to_100(self):
        self.thing.quantity=100
        self._assert_thing_is_valid()
   