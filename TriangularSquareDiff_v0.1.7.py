"""
Triangular Number Analysis Program
Finds numbers that are both:
1. Sum of two consecutive triangular numbers (T_n + T_(n+1))
2. Difference of two triangular numbers (T_m - T_k)

Special focus: Finding the smallest ODD number with both properties
Mathematical derivation: Multiple subscript expression for (T_(T_n²))²

Uses the property: T_n + T_(n+1) = (n+1)²

Author: Gregory Conner
Version: 0.1.7
"""

import math

def derive_multiple_subscript_expression(n):
    """
    Derive a multiple subscript expression for (T_(T_n²))² using the consecutive sum property.
    
    Mathematical derivation:
    1. Start with T_n²
    2. T_(T_n²) = T_(T_n²) (triangular number of the square)
    3. (T_(T_n²))² = (T_(T_n²))² (square of the result)
    
    Using the property T_k + T_(k+1) = (k+1)²:
    If T_(T_n²) = m, then T_(T_n²) + T_(T_n² + 1) = (T_n² + 1)²
    
    But we want (T_(T_n²))², not T_(T_n²) + T_(T_n² + 1)
    
    Let's work backwards: if we want (T_(T_n²))², we need to find consecutive triangulars that sum to T_(T_n²)
    
    If T_(T_n²) = k² for some k, then T_(T_n²) = T_(k-1) + T_k
    So (T_(T_n²))² = (T_(k-1) + T_k)² = k⁴
    
    But this doesn't give us a multiple subscript expression directly.
    
    Let's try a different approach: express T_(T_n²) as a sum of consecutive triangulars.
    """
    T_n = triangular_number(n)
    T_n_squared = T_n * T_n
    T_of_T_n_squared = triangular_number(T_n_squared)
    
    print(f"Mathematical Derivation for n = {n}:")
    print(f"T_{n} = {T_n}")
    print(f"T_{n}² = {T_n_squared}")
    print(f"T_{T_n_squared} = {T_of_T_n_squared}")
    print(f"(T_{T_n_squared})² = {T_of_T_n_squared ** 2}")
    print()
    
    # Check if T_(T_n²) is a perfect square
    if is_perfect_square(T_of_T_n_squared):
        sqrt_val = int(math.sqrt(T_of_T_n_squared))
        print(f"Since T_{T_n_squared} = {T_of_T_n_squared} = {sqrt_val}²,")
        print(f"we have T_{T_n_squared} = T_{sqrt_val-1} + T_{sqrt_val}")
        print(f"Therefore: (T_{T_n_squared})² = ({sqrt_val}²)² = {sqrt_val}⁴ = {sqrt_val**4}")
        print()
        
        # Verify the consecutive sum
        T_k_minus_1 = triangular_number(sqrt_val - 1)
        T_k = triangular_number(sqrt_val)
        print(f"Verification: T_{sqrt_val-1} + T_{sqrt_val} = {T_k_minus_1} + {T_k} = {T_k_minus_1 + T_k}")
        print(f"Check: {T_k_minus_1 + T_k} = {sqrt_val}² = {sqrt_val**2} ✓")
        print()
        
        return sqrt_val, sqrt_val - 1, sqrt_val
    else:
        print(f"T_{T_n_squared} = {T_of_T_n_squared} is not a perfect square")
        print("Cannot express as sum of consecutive triangular numbers using the property")
        return None, None, None

def general_multiple_subscript_derivation(n):
    """
    General derivation for (T_(T_n²))² using the consecutive sum property.
    
    Key insight: Even when T_(T_n²) is not a perfect square, we can still use
    the consecutive sum property in a different way.
    
    If we want (T_(T_n²))², and T_(T_n²) = m, then:
    (T_(T_n²))² = m²
    
    Now, if m = T_k + T_(k+1) for some k, then:
    m² = (T_k + T_(k+1))² = (k+1)⁴
    
    But we need to find k such that T_k + T_(k+1) = T_(T_n²)
    This means: (k+1)² = T_(T_n²)
    So: k+1 = √(T_(T_n²))
    
    This only works if T_(T_n²) is a perfect square.
    
    For the general case, we can express (T_(T_n²))² as:
    (T_(T_n²))² = (T_(T_n²))² = (T_(T_n²))²
    
    But we can also use the fact that:
    T_(T_n²) = T_n²(T_n² + 1)/2
    
    So: (T_(T_n²))² = (T_n²(T_n² + 1)/2)² = T_n⁴(T_n² + 1)²/4
    """
    T_n = triangular_number(n)
    T_n_squared = T_n * T_n
    T_of_T_n_squared = triangular_number(T_n_squared)
    
    print(f"General Derivation for n = {n}:")
    print(f"T_{n} = {T_n}")
    print(f"T_{n}² = {T_n_squared}")
    print(f"T_{T_n_squared} = {T_of_T_n_squared}")
    print(f"(T_{T_n_squared})² = {T_of_T_n_squared ** 2}")
    print()
    
    # Direct formula
    direct_formula = (T_n_squared * (T_n_squared + 1) // 2) ** 2
    print(f"Direct formula: (T_{T_n_squared})² = (T_{T_n_squared})² = {direct_formula}")
    print()
    
    # Alternative expression using the triangular number formula
    alt_formula = (T_n_squared * (T_n_squared + 1) // 2) ** 2
    print(f"Using T_k = k(k+1)/2: T_{T_n_squared} = {T_n_squared}({T_n_squared}+1)/2 = {T_of_T_n_squared}")
    print(f"Therefore: (T_{T_n_squared})² = ({T_of_T_n_squared})² = {alt_formula}")
    print()
    
    # Check if we can use consecutive sum property
    if is_perfect_square(T_of_T_n_squared):
        sqrt_val = int(math.sqrt(T_of_T_n_squared))
        print(f"Since T_{T_n_squared} = {T_of_T_n_squared} = {sqrt_val}²,")
        print(f"we can use consecutive sum property:")
        print(f"T_{T_n_squared} = T_{sqrt_val-1} + T_{sqrt_val}")
        print(f"Therefore: (T_{T_n_squared})² = ({sqrt_val}²)² = {sqrt_val}⁴")
        return sqrt_val
    else:
        print(f"T_{T_n_squared} = {T_of_T_n_squared} is not a perfect square")
        print("Cannot directly apply consecutive sum property")
        return None

def demonstrate_multiple_subscript_derivation():
    """Demonstrate the multiple subscript expression derivation for small values"""
    print("Multiple Subscript Expression Derivation")
    print("=" * 50)
    print()
    print("Using the property: T_k + T_(k+1) = (k+1)²")
    print("We can derive expressions for (T_(T_n²))²")
    print()
    
    for n in range(1, 6):
        result = derive_multiple_subscript_expression(n)
        if result[0] is not None:
            sqrt_val, k_minus_1, k = result
            print(f"For n={n}: (T_(T_{n}²))² = (T_{triangular_number(n)**2})² = {sqrt_val}⁴")
        print("-" * 40)
    
    print("\nGeneral Derivation (works for all cases):")
    print("=" * 50)
    for n in range(1, 6):
        general_multiple_subscript_derivation(n)
        print("-" * 40)

def consecutive_triangular_sum_property(n):
    """
    Demonstrate the property: T_n + T_(n+1) = (n+1)²
    Returns (T_n, T_(n+1), sum, (n+1)², is_valid)
    """
    T_n = triangular_number(n)
    T_n_plus_1 = triangular_number(n + 1)
    sum_consecutive = T_n + T_n_plus_1
    square_of_next = (n + 1) ** 2
    is_valid = sum_consecutive == square_of_next
    
    return T_n, T_n_plus_1, sum_consecutive, square_of_next, is_valid

def is_sum_of_consecutive_triangulars(x):
    """
    Check if a number is the sum of two consecutive triangular numbers.
    Uses the property: T_n + T_(n+1) = (n+1)²
    So if x = k², then x = T_(k-1) + T_k
    Returns (is_sum, n) where x = T_n + T_(n+1)
    """
    if not is_perfect_square(x):
        return False, 0
    
    sqrt_x = int(math.sqrt(x))
    n = sqrt_x - 1  # Since T_n + T_(n+1) = (n+1)², if x = k², then n = k-1
    
    if n > 0:
        T_n = triangular_number(n)
        T_n_plus_1 = triangular_number(n + 1)
        if T_n + T_n_plus_1 == x:
            return True, n
    
    return False, 0

def demonstrate_consecutive_property(max_n=10):
    """Demonstrate the consecutive triangular sum property for values 1 to max_n"""
    print("Demonstrating the property: T_n + T_(n+1) = (n+1)²")
    print("=" * 50)
    
    for n in range(1, max_n + 1):
        T_n, T_n_plus_1, sum_val, square_val, is_valid = consecutive_triangular_sum_property(n)
        print(f"n={n:2d}: T_{n} + T_{n+1} = {T_n:2d} + {T_n_plus_1:2d} = {sum_val:2d} = {n+1}² = {square_val:2d} ✓" if is_valid else f"n={n:2d}: ERROR!")
    
    print()

def triangular_number(n):
    """Calculate the nth triangular number: T_n = n(n+1)/2"""
    return n * (n + 1) // 2

def is_perfect_square(x):
    """Check if a number is a perfect square"""
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x

def is_square_of_triangular_of_square_of_triangular(x):
    """
    Check if a number is the square of the triangular number of the square of a triangular number.
    This means x = (T_(T_n²))² for some n.
    Returns (is_square_of_triangular_of_square_of_triangular, n) where n is the triangular number index.
    """
    # We need to find n such that x = (T_(T_n²))²
    # This means x = (T_n² * (T_n² + 1) / 2)²
    
    # First check if x is a perfect square
    if not is_perfect_square(x):
        return False, 0
    
    sqrt_x = int(math.sqrt(x))
    
    # Try different values of n to see if sqrt_x = T_(T_n²)
    max_n = 10  # Even smaller bound since this grows very quickly
    
    for n in range(1, max_n + 1):
        T_n = triangular_number(n)
        T_n_squared = T_n * T_n
        T_of_T_n_squared = triangular_number(T_n_squared)
        
        if T_of_T_n_squared == sqrt_x:
            return True, n
        elif T_of_T_n_squared > sqrt_x:
            break  # No point continuing if we've exceeded sqrt_x
    
    return False, 0

def is_triangular_of_square_of_triangular(x):
    """
    Check if a number is the triangular number of the square of a triangular number.
    This means x = T_(T_n²) for some n.
    Returns (is_triangular_of_square_of_triangular, n) where n is the triangular number index.
    """
    # We need to find n such that x = T_(T_n²)
    # This means x = T_n² * (T_n² + 1) / 2
    
    # Try different values of n
    max_n = 20  # Reasonable upper bound since T_n² grows quickly
    
    for n in range(1, max_n + 1):
        T_n = triangular_number(n)
        T_n_squared = T_n * T_n
        T_of_T_n_squared = triangular_number(T_n_squared)
        
        if T_of_T_n_squared == x:
            return True, n
        elif T_of_T_n_squared > x:
            break  # No point continuing if we've exceeded x
    
    return False, 0

def is_square_of_triangular(x):
    """
    Check if a number is the square of a triangular number.
    Returns (is_square_of_triangular, n) where n is the triangular number index.
    """
    if not is_perfect_square(x):
        return False, 0
    
    sqrt_x = int(math.sqrt(x))
    
    # Check if sqrt_x is a triangular number
    # We need to solve: sqrt_x = n(n+1)/2
    # This gives us: 2*sqrt_x = n(n+1)
    # Rearranging: n² + n - 2*sqrt_x = 0
    # Using quadratic formula: n = (-1 ± √(1 + 8*sqrt_x))/2
    
    discriminant = 1 + 8 * sqrt_x
    if not is_perfect_square(discriminant):
        return False, 0
    
    sqrt_discriminant = int(math.sqrt(discriminant))
    n1 = (-1 + sqrt_discriminant) // 2
    n2 = (-1 - sqrt_discriminant) // 2
    
    # Take the positive solution
    n = max(n1, n2)
    
    if n > 0 and triangular_number(n) == sqrt_x:
        return True, n
    
    return False, 0

def is_difference_of_triangulars(x):
    """
    Check if a number is the difference between two triangular numbers.
    Returns (is_difference, n, m) where T_m - T_n = x
    """
    # We need to find m, n such that T_m - T_n = x
    # T_m - T_n = m(m+1)/2 - n(n+1)/2 = (m² + m - n² - n)/2
    # = ((m-n)(m+n+1))/2
    
    # For each possible n, try to find m
    max_n = 1000  # Reasonable upper bound
    
    for n in range(1, max_n + 1):
        T_n = triangular_number(n)
        # We need T_m = T_n + x
        target_T_m = T_n + x
        
        # Check if target_T_m is a triangular number
        # Solve: target_T_m = m(m+1)/2
        # This gives: m² + m - 2*target_T_m = 0
        discriminant = 1 + 8 * target_T_m
        
        if is_perfect_square(discriminant):
            sqrt_discriminant = int(math.sqrt(discriminant))
            m1 = (-1 + sqrt_discriminant) // 2
            m2 = (-1 - sqrt_discriminant) // 2
            
            m = max(m1, m2)
            
            if m > n and triangular_number(m) == target_T_m:
                return True, n, m
    
    return False, 0, 0

def find_smallest_odd_consecutive_sum_and_difference():
    """Find the smallest ODD number that is both sum of consecutive triangulars and difference of triangulars"""
    print("Triangular Number Analysis: Smallest ODD Consecutive Sum AND Difference")
    print("=" * 70)
    print()
    
    # Demonstrate the consecutive triangular sum property
    demonstrate_consecutive_property(10)
    
    print("Searching for the smallest ODD natural number that is:")
    print("1. Sum of two consecutive triangular numbers (T_n + T_(n+1))")
    print("2. Difference of two triangular numbers (T_m - T_k)")
    print()
    
    # Since T_n + T_(n+1) = (n+1)², we only need to check perfect squares
    # For odd numbers, we need odd perfect squares: 3², 5², 7², 9², ...
    # Start searching from odd perfect squares
    for n in range(3, 100, 2):  # Start from n=3 (odd), step by 2 to get only odd numbers
        x = n * n  # This is T_(n-1) + T_n
        
        # Check if x is also difference of triangulars
        is_diff_tri, k, m = is_difference_of_triangulars(x)
        
        if is_diff_tri:
            print(f"Found solution: {x}")
            print(f"  - {x} = T_{n-1} + T_{n} = {triangular_number(n-1)} + {triangular_number(n)} = {n}²")
            print(f"  - {x} = T_{m} - T_{k} = {triangular_number(m)} - {triangular_number(k)}")
            return x, n-1, n, k, m
        
        # Progress indicator
        if n % 10 == 1:  # Show progress every 10 odd numbers
            print(f"Checked odd perfect squares up to {n}² = {x}...")
    
    print("No solution found in the search range.")
    return None

def find_smallest_consecutive_sum_and_difference():
    """Find the smallest number that is both sum of consecutive triangulars and difference of triangulars"""
    print("Triangular Number Analysis: Consecutive Sum AND Difference")
    print("=" * 60)
    print()
    
    # Demonstrate the consecutive triangular sum property
    demonstrate_consecutive_property(10)
    
    print("Searching for the smallest natural number that is:")
    print("1. Sum of two consecutive triangular numbers (T_n + T_(n+1))")
    print("2. Difference of two triangular numbers (T_m - T_k)")
    print()
    
    # Since T_n + T_(n+1) = (n+1)², we only need to check perfect squares
    # Start searching from small perfect squares
    for n in range(2, 100):  # Start from n=2 since n=1 gives 4, which is small
        x = n * n  # This is T_(n-1) + T_n
        
        # Check if x is also difference of triangulars
        is_diff_tri, k, m = is_difference_of_triangulars(x)
        
        if is_diff_tri:
            print(f"Found solution: {x}")
            print(f"  - {x} = T_{n-1} + T_{n} = {triangular_number(n-1)} + {triangular_number(n)} = {n}²")
            print(f"  - {x} = T_{m} - T_{k} = {triangular_number(m)} - {triangular_number(k)}")
            return x, n-1, n, k, m
        
        # Progress indicator
        if n % 10 == 0:
            print(f"Checked perfect squares up to {n}² = {x}...")
    
    print("No solution found in the search range.")
    return None

def find_smallest_solution():
    """Find the smallest natural number satisfying both conditions"""
    print("Triangular Number Analysis with Consecutive Sum Property")
    print("=" * 60)
    print()
    
    # Demonstrate the consecutive triangular sum property
    demonstrate_consecutive_property(10)
    
    print("Searching for the smallest natural number that is:")
    print("1. The square of the triangular number of the square of a triangular number ((T_(T_n²))²)")
    print("2. The difference between two triangular numbers (T_m - T_k)")
    print()
    
    # Start searching from small numbers
    for x in range(1, 1000001):  # Increased search range significantly
        # Check if x is square of triangular of square of triangular
        is_square_tri_of_square_tri, n1 = is_square_of_triangular_of_square_of_triangular(x)
        
        if is_square_tri_of_square_tri:
            # Check if x is difference of triangulars
            is_diff_tri, n2, m = is_difference_of_triangulars(x)
            
            if is_diff_tri:
                T_n1 = triangular_number(n1)
                T_n1_squared = T_n1 * T_n1
                T_of_T_n1_squared = triangular_number(T_n1_squared)
                
                # Check if x is also sum of consecutive triangulars
                is_consec_sum, n_consec = is_sum_of_consecutive_triangulars(x)
                
                print(f"Found solution: {x}")
                print(f"  - {x} = {T_of_T_n1_squared}² (where T_{n1} = {T_n1}, T_{T_n1_squared} = {T_of_T_n1_squared})")
                print(f"  - {x} = T_{m} - T_{n2} = {triangular_number(m)} - {triangular_number(n2)}")
                
                if is_consec_sum:
                    print(f"  - {x} = T_{n_consec} + T_{n_consec+1} = {triangular_number(n_consec)} + {triangular_number(n_consec+1)} (using consecutive property)")
                
                return x, n1, n2, m
        
        # Progress indicator
        if x % 100000 == 0:
            print(f"Checked up to {x}...")
    
    print("No solution found in the search range.")
    return None

if __name__ == "__main__":
    # Demonstrate the multiple subscript expression derivation
    demonstrate_multiple_subscript_derivation()
    
    print("\n" + "="*70 + "\n")
    
    # Also run the original problem
    result = find_smallest_odd_consecutive_sum_and_difference()
