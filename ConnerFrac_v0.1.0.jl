"""
Triangular Number Analysis Program
Finds the smallest natural number that is both:
1. The square of a triangular number
2. The difference between two triangular numbers

Author: Gregory Conner
Version: 0.1.0
"""

# Triangular number formula: T_n = n(n+1)/2
function triangular_number(n::Int)
    return n * (n + 1) ÷ 2
end

# Check if a number is a perfect square
function is_perfect_square(x::Int)
    if x < 0
        return false
    end
    root = isqrt(x)
    return root * root == x
end

# Check if a number is the square of a triangular number
function is_square_of_triangular(x::Int)
    if !is_perfect_square(x)
        return false, 0
    end
    
    sqrt_x = isqrt(x)
    
    # Check if sqrt_x is a triangular number
    # We need to solve: sqrt_x = n(n+1)/2
    # This gives us: 2*sqrt_x = n(n+1)
    # Rearranging: n² + n - 2*sqrt_x = 0
    # Using quadratic formula: n = (-1 ± √(1 + 8*sqrt_x))/2
    
    discriminant = 1 + 8 * sqrt_x
    if !is_perfect_square(discriminant)
        return false, 0
    end
    
    sqrt_discriminant = isqrt(discriminant)
    n1 = (-1 + sqrt_discriminant) ÷ 2
    n2 = (-1 - sqrt_discriminant) ÷ 2
    
    # Take the positive solution
    n = max(n1, n2)
    
    if n > 0 && triangular_number(n) == sqrt_x
        return true, n
    end
    
    return false, 0
end

# Check if a number is the difference between two triangular numbers
function is_difference_of_triangulars(x::Int)
    # We need to find m, n such that T_m - T_n = x
    # T_m - T_n = m(m+1)/2 - n(n+1)/2 = (m² + m - n² - n)/2
    # = ((m-n)(m+n+1))/2
    
    # For each possible n, try to find m
    max_n = 1000  # Reasonable upper bound
    
    for n in 1:max_n
        T_n = triangular_number(n)
        # We need T_m = T_n + x
        target_T_m = T_n + x
        
        # Check if target_T_m is a triangular number
        # Solve: target_T_m = m(m+1)/2
        # This gives: m² + m - 2*target_T_m = 0
        discriminant = 1 + 8 * target_T_m
        
        if is_perfect_square(discriminant)
            sqrt_discriminant = isqrt(discriminant)
            m1 = (-1 + sqrt_discriminant) ÷ 2
            m2 = (-1 - sqrt_discriminant) ÷ 2
            
            m = max(m1, m2)
            
            if m > n && triangular_number(m) == target_T_m
                return true, n, m
            end
        end
    end
    
    return false, 0, 0
end

# Main function to find the smallest number satisfying both conditions
function find_smallest_solution()
    println("Searching for the smallest natural number that is:")
    println("1. The square of a triangular number")
    println("2. The difference between two triangular numbers")
    println()
    
    # Start searching from small numbers
    for x in 1:10000
        # Check if x is square of triangular
        is_square_tri, n1 = is_square_of_triangular(x)
        
        if is_square_tri
            # Check if x is difference of triangulars
            is_diff_tri, n2, m = is_difference_of_triangulars(x)
            
            if is_diff_tri
                println("Found solution: $x")
                println("  - $x = $(triangular_number(n1))² (where T_$n1 = $(triangular_number(n1)))")
                println("  - $x = T_$m - T_$n2 = $(triangular_number(m)) - $(triangular_number(n2))")
                return x, n1, n2, m
            end
        end
        
        # Progress indicator
        if x % 1000 == 0
            println("Checked up to $x...")
        end
    end
    
    println("No solution found in the search range.")
    return nothing
end

# Run the main function
if abspath(PROGRAM_FILE) == @__FILE__
    result = find_smallest_solution()
end
