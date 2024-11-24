from django.test import TestCase
from myapp.models import katalog
# Create your tests here.
class KatalogTesstCase(TestCase):
    def setUp(self):
        katalog.objects.create(cost = 100000)
        katalog.objects.create(cost = 123444)
    def test_cost_procent(self):
        sum1 = katalog.objects.get(id = 1)
        sum2 = katalog.objects.get(id = 2 )
        self.assertEqual(sum1.procent(10),10000)
        self.assertEqual(sum2.procent(37), 40000)
