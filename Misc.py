def max_path_down_triangle(triangle_str):
    '''
    Solution for problems 18 and 67
    '''
    # parse the triange_str in to a usable form
    triangle = []
    for line in triangle_str.split('\n'):
        if line:
            triangle.append([int(num) for num in line.split(' ') if num])
    if len(triangle) > 1:
        # work top to bottom, memoizing the max path to that point
        for line_index in range(1, len(triangle)):
            current_line = triangle[line_index]
            for i in range(0, len(current_line)):
                if i == 0:
                    current_line[i] += triangle[line_index - 1][i]
                elif i == len(current_line) - 1:
                    current_line[i] += triangle[line_index - 1][i - 1]
                else:
                    upper_left = triangle[line_index - 1][i]
                    upper_right = triangle[line_index - 1][i - 1]
                    current_line[i] += max(upper_left, upper_right)
    return max(triangle[len(triangle) - 1])


if __name__ == '__main__':
    import unittest

    class Tests(unittest.TestCase):
        def test_math_path_down_triangle(self):
            cases = [{
                'triangle_str': 
'''
3
7 4
2 4 6
8 5 9 3
''', 'answer': 23
            }]
            for case in cases:
                triangle_str = case['triangle_str']
                expected = case['answer']
                with self.subTest(triangle_str=triangle_str, expected=expected):
                    answer = max_path_down_triangle(triangle_str)
                    self.assertEqual(expected, answer)

    unittest.main()