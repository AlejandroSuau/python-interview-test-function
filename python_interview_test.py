# -*- coding: utf-8 -*-

import unittest

def calculate_products(numbers = []):
    if not numbers or len(numbers) < 2:
        print("List of numbers has an incorrect definition.")
        return []
    
    result = []
    
    i = 0
    a = 0
    numbers_quantity = len(numbers)
    while i < numbers_quantity:
        product_number = 1
        producted_numbers = 0
        a = i + 1

        while producted_numbers < (numbers_quantity-1):
            if a >= numbers_quantity:
                a = 0
            
            product_number *= numbers[a]
            producted_numbers += 1
            a += 1
        
        result.append(product_number)
        i += 1
    
    return result

class CalculateProductFunction(unittest.TestCase):
    
    def test_basic_numbers_empty_list(self):
        numbers = []
        result = calculate_products(numbers)
        expected_result = []
        self.assertEqual(result, expected_result)
    
    def test_basic_numbers_insufficient_numbers(self):
        numbers = []
        result = calculate_products(numbers)
        expected_result = []
        self.assertEqual(result, expected_result)
    
    def test_basic_numbers_product_1(self):
        numbers = [1, 5]
        result = calculate_products(numbers)
        expected_result = [5, 1]
        self.assertEqual(result, expected_result)
    
    def test_basic_numbers_product_2(self):
        numbers = [1, 5, 7]
        result = calculate_products(numbers)
        expected_result = [35, 7, 5]
        self.assertEqual(result, expected_result)
        
    def test_basic_numbers_product_3(self):
        numbers = [1, 5, 7, 2]
        result = calculate_products(numbers)
        expected_result = [70, 14, 10, 35]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(CalculateProductFunction)
    all_tests_suite = unittest.TestSuite(suite)
    
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)
