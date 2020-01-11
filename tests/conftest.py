import pytest
from .. import scrapper

@pytest.fixture(scope="session")
def swiper():
	return scrapper.Scrapper()