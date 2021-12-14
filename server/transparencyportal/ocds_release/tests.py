from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CustomEndpointTests(APITestCase):
    fixtures = ['dump_data.json']

    def test_record_item_list(self):
        """
        Ensure record item list endpoint is reachable
        """
        url = reverse('api:record-item-list', kwargs={'record_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_record_stage_list(self):
        """
        Ensure record stage list endpoint is reachable
        """
        url = reverse('api:record-stage-list', kwargs={'record_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buyer_records_inprogress(self):
        """
        Ensure buyer in_progress records endpoint is reachable
        """
        url = reverse('api:buyer-records-inprogress', kwargs={'buyer_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buyer_records_done(self):
        """
        Ensure buyer done records stage list endpoint is reachable
        """
        url = reverse('api:buyer-records-done', kwargs={'buyer_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_buyer_project_totalbyregion(self):
        """
        Ensure buyer project total_by_region endpoint is reachable
        """
        url = reverse('api:buyer-project-totalbyregion', kwargs={'buyer_id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NotFoundCustomEndpointTests(APITestCase):

    def test_record_item_list(self):
        """
        Ensure record item list endpoint returns 404 Response if not found
        """
        url = reverse('api:record-item-list', kwargs={'record_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_record_stage_list(self):
        """
        Ensure record stage list endpoint returns 404 Response if not found
        """
        url = reverse('api:record-stage-list', kwargs={'record_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_buyer_records_inprogress(self):
        """
        Ensure buyer in_progress records endpoint returns 404 Response if not found
        """
        url = reverse('api:buyer-records-inprogress', kwargs={'buyer_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_buyer_records_done(self):
        """
        Ensure buyer done records stage list endpoint returns 404 Response if not found
        """
        url = reverse('api:buyer-records-done', kwargs={'buyer_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_buyer_project_totalbyregion(self):
        """
        Ensure buyer project total_by_region endpoint returns 404 Response if not found
        """
        url = reverse('api:buyer-project-totalbyregion', kwargs={'buyer_id': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
