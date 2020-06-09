import unittest


from Code.datamunger import check_row
from Code.datamunger import check_monotonic
from Code.datamunger import calc_total


class CheckRowTestCase(unittest.TestCase):

	def test_check_row_correct(self):
		prev = (0,0,0,0,0,0,0,0,0,0)
		curr = ("36","1","2","3","4","5","6","7","8","0")
		n=2
		result = check_row(n,prev,curr)
		self.assertEqual(result, True)

	def test_check_row_wrong(self):
		prev = (0,0,0,0,0,0,0,0,0,0)
		curr = ("36","1","2","3","Test","5","6","7","8","0")
		n=2
		result = check_row(n,prev,curr)
		self.assertEqual(result, False)

	def test_check_row_zero(self):
		prev = (0,0,0,0,0,0,0,0,0,0)
		curr = (0,0,0,0,0,0,0,0,0,0)
		n=2
		result = check_row(n,prev,curr)
		self.assertEqual(result, True)

	def test_calc_total_correct_first(self):
		curr = (52,3,4,5,6,7,8,9,10,0)
		result = calc_total(curr)
		self.assertEqual(result,52)

	def test_calc_total_correct_second(self):
		curr = (8,1,1,1,1,1,1,1,1,0)
		result = calc_total(curr)
		self.assertEqual(result,8)



if __name__ == '__main__':
	unittest.main()
