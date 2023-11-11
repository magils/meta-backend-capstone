from django.test import TestCase

class MenuItemTest(TestCase):   
   def test_get_item(self):
      item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
      self.assertEqual(item, "IceCream : 80")


class BookingTest(TestCase):
   def test_create_booking(self):
      booking = Booking.objects.create(
         name = "Test Booking",
         no_of_guest = 5,
         booking_date = datetime.now()
      )
      
      self.assertEqual(booking.name, "Test Booking")
      self.assertEqual(booking.no_of_guest, 5)