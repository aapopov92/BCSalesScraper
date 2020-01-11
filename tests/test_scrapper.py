import pytest

class TestScrapper:

	def test_correct_product_dict_structure_is_returned(self, swiper):
		keys = ['id', 'discount', 'price', 'brand', 'name', 'url', 'image']
		result = swiper.scrape('https://www.backcountry.com', '/whitewater-paddles')
		assert keys == list(result[0].keys()), 'Incorrect dict structure is returned from scrapper'

	def test_correct_error_is_raised_for_base_url(self, swiper):
		with pytest.raises(TypeError):
			swiper.scrape(1, 's')

	def test_correct_error_is_raised_for_page(self, swiper):
		with pytest.raises(TypeError):
			swiper.scrape('1', 2)

	def test_non_empty_response_returned_for_correct_page(self, swiper):
		result = swiper.scrape('https://www.backcountry.com', '/whitewater-paddles')
		assert len(result) > 0, 'Empty result returned for paddles. No more paddles? O_o'
