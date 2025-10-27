"""
Triangular Square Difference Finder
Finds the smallest natural number that is both:
1. The square of the triangular number of the square of a triangular number ((T_(T_n²))²)
2. The difference between two triangular numbers (T_m - T_k)

Uses the property: T_n + T_(n+1) = (n+1)²

Author: Gregory Conner
Version: 0.1.4
"""

import math

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
    result = find_smallest_solution()
