from django.test import TestCase, Client as TestClient  # Alias to avoid conflict
from django.urls import reverse
from accounts.models import CustomUser
from .models import Dispatch
from .forms import DispatchForm, DispatchStatusForm
from clients.models import Client
from drivers.models import Driver

class DispatchTests(TestCase):
    def setUp(self):
        # Set up test client and test data
        self.test_client = TestClient()  # Renamed to avoid conflict with Client model
        # Create a test user (client role) and client
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass123',
            role='client'  # Required field
        )
        self.client_obj = Client.objects.create(user=self.user)
        # Create a test user (driver role) and driver
        self.driver_user = CustomUser.objects.create_user(
            username='driver',
            password='driverpass123',
            role='driver'  # Required field
        )
        self.driver = Driver.objects.create(user=self.driver_user)
        # Create a test dispatch
        self.dispatch = Dispatch.objects.create(
            client=self.client_obj,
            driver=self.driver,
            status='PENDING',
            pickup_location='123 Pickup St',
            dropoff_location='456 Dropoff Ave'
        )

    def test_dispatch_model(self):
        # Test the Dispatch model string representation
        # Updated to match your actual _str_ (adjust if needed)
        self.assertEqual(str(self.dispatch), f"Dispatch {self.dispatch.id} - {self.dispatch.status}")

    def test_dispatch_list_view(self):
        # Test the dispatch list view
        response = self.test_client.get(reverse('dispatch_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dispatches/dispatch_list.html')
        self.assertContains(response, self.client_obj.user.username)

    def test_create_dispatch_view_get(self):
        # Test accessing the create dispatch page (GET request)
        self.test_client.login(username='testuser', password='testpass123')
        response = self.test_client.get(reverse('create_dispatch'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dispatches/create_dispatch.html')
        self.assertIsInstance(response.context['form'], DispatchForm)

    def test_create_dispatch_view_post(self):
        # Test creating a new dispatch (POST request)
        self.test_client.login(username='testuser', password='testpass123')
        data = {
            'client': self.client_obj.id,
            'driver': self.driver.id,
            'status': 'PENDING',
            'pickup_location': '789 Test Rd',
            'dropoff_location': '101 Test Blvd'
        }
        response = self.test_client.post(reverse('create_dispatch'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST
        self.assertEqual(Dispatch.objects.count(), 2)  # One from setUp, one created
        self.assertTrue(Dispatch.objects.filter(pickup_location='789 Test Rd').exists())

    def test_dispatch_detail_view(self):
        # Test the dispatch detail view
        self.test_client.login(username='testuser', password='testpass123')
        response = self.test_client.get(reverse('dispatch_detail', args=[self.dispatch.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dispatches/dispatch_detail.html')
        self.assertContains(response, self.dispatch.pickup_location)

    def test_dispatch_detail_update_status(self):
        # Test updating dispatch status
        self.test_client.login(username='testuser', password='testpass123')
        data = {'status': 'IN_PROGRESS'}
        response = self.test_client.post(reverse('dispatch_detail', args=[self.dispatch.id]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful POST
        self.dispatch.refresh_from_db()
        self.assertEqual(self.dispatch.status, 'IN_PROGRESS')
