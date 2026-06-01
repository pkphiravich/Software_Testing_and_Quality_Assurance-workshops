import pytest
from unittest.mock import patch, Mock
from cart import Cart, MAX_QUANTITY_PER_PRODUCT


@pytest.fixture
def setup():
	cart_obj = Cart()
	yield cart_obj

def test_add_product_to_cart(capsys, setup):
	setup.add_to_cart("apple")
	stdout = capsys.readouterr()
	assert "apple successfully added to cart. Quantity now: 1" in stdout.out

def test_exceed_max_quantity_per_product(setup):

	i = 0
	while i < (MAX_QUANTITY_PER_PRODUCT + 1):
		setup.add_to_cart("apple")
		i += 1
		if i == 5:
			break

	with pytest.raises(Exception) as exc:
		setup.add_to_cart("apple")
		assert str(exc.value) == f"You can't add more than {MAX_QUANTITY_PER_PRODUCT} items per product"

def test_total_price_empty_cart(setup):

	assert setup.total_price() == 0.0



@patch('cart.ProductDatabase')
def test_total_price_with_items(mock_product_db, setup):
	# setup.carts = {"apple": 1, "banana": 2, "orange": 3} -> dangerous
	setup.add_to_cart("apple")
	setup.add_to_cart("banana")
	setup.add_to_cart("banana")
	setup.add_to_cart("orange")
	setup.add_to_cart("orange")
	setup.add_to_cart("orange")
	

	def mock_get_price(fruits):
		prices = {"apple": 15, "banana": 10, "orange": 5}
		return prices[fruits]
	
	mock_product_db.return_value.get_price.side_effect = mock_get_price

	total = setup.total_price()
	assert total == 50



