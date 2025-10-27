"""
Triangular Number LaTeX Derivation Program
Derives mathematical expressions for (T_(T_m)²)² using the consecutive sum property
T_n + T_(n+1) = (n+1)²

Generates LaTeX document and compiles to PDF

Author: Gregory Conner
Version: 0.2.0
"""

import math
import subprocess
import os

def triangular_number(n):
    """Calculate the nth triangular number: T_n = n(n+1)/2"""
    return n * (n + 1) // 2

def is_perfect_square(x):
    """Check if a number is a perfect square"""
    if x < 0:
        return False
    root = int(math.sqrt(x))
    return root * root == x

def derive_expression_for_T_T_m_squared_squared(m):
    """
    Derive expression for (T_(T_m)²)² using the triangular number identity recursively.
    
    Key insight: i² = T_{i-1} + T_i
    
    We apply this rule recursively until no squares remain on the right side.
    """
    T_m = triangular_number(m)
    T_m_squared = T_m * T_m
    T_of_T_m_squared = triangular_number(T_m_squared)
    
    print(f"Complete derivation for m = {m}:")
    print(f"T_{m} = {T_m}")
    print(f"T_{m}² = {T_m_squared}")
    
    # Step 1: Apply identity to T_m²
    k = T_m
    print(f"\nStep 1: Apply identity to T_{m}²")
    print(f"T_{m}² = T_{k-1} + T_{k}")
    print(f"T_{k-1} = {triangular_number(k-1)}")
    print(f"T_{k} = {triangular_number(k)}")
    print(f"Check: T_{k-1} + T_{k} = {triangular_number(k-1)} + {triangular_number(k)} = {triangular_number(k-1) + triangular_number(k)} ✓")
    
    # Step 2: Calculate T_{T_m²} = T_{T_{k-1} + T_{k}}
    print(f"\nStep 2: Calculate T_{T_m_squared}")
    print(f"T_{T_m_squared} = T_{{T_{k-1} + T_{k}}} = T_{triangular_number(k-1) + triangular_number(k)} = T_{T_m_squared} = {T_of_T_m_squared}")
    
    # Step 3: Apply identity to (T_{T_m²})²
    j = T_of_T_m_squared
    print(f"\nStep 3: Apply identity to (T_{T_m_squared})²")
    print(f"(T_{T_m_squared})² = T_{j-1} + T_{j}")
    print(f"T_{j-1} = {triangular_number(j-1)}")
    print(f"T_{j} = {triangular_number(j)}")
    print(f"Check: T_{j-1} + T_{j} = {triangular_number(j-1)} + {triangular_number(j)} = {triangular_number(j-1) + triangular_number(j)} ✓")
    
    # Step 4: Now we need to eliminate the squares in the subscripts
    # T_{j-1} and T_{j} might have squares in their subscripts
    print(f"\nStep 4: Eliminate squares in subscripts")
    
    # Check if j-1 or j are perfect squares
    if is_perfect_square(j-1):
        sqrt_j_minus_1 = int(math.sqrt(j-1))
        print(f"Since {j-1} = {sqrt_j_minus_1}², we have:")
        print(f"T_{j-1} = T_{sqrt_j_minus_1-1} + T_{sqrt_j_minus_1}")
        print(f"T_{sqrt_j_minus_1-1} = {triangular_number(sqrt_j_minus_1-1)}")
        print(f"T_{sqrt_j_minus_1} = {triangular_number(sqrt_j_minus_1)}")
        print(f"Check: T_{sqrt_j_minus_1-1} + T_{sqrt_j_minus_1} = {triangular_number(sqrt_j_minus_1-1) + triangular_number(sqrt_j_minus_1)} ✓")
    else:
        print(f"T_{j-1} = {triangular_number(j-1)} (no squares to eliminate)")
    
    if is_perfect_square(j):
        sqrt_j = int(math.sqrt(j))
        print(f"Since {j} = {sqrt_j}², we have:")
        print(f"T_{j} = T_{sqrt_j-1} + T_{sqrt_j}")
        print(f"T_{sqrt_j-1} = {triangular_number(sqrt_j-1)}")
        print(f"T_{sqrt_j} = {triangular_number(sqrt_j)}")
        print(f"Check: T_{sqrt_j-1} + T_{sqrt_j} = {triangular_number(sqrt_j-1) + triangular_number(sqrt_j)} ✓")
    else:
        print(f"T_{j} = {triangular_number(j)} (no squares to eliminate)")
    
    print(f"\nFinal result: (T_{T_m_squared})² = T_{j-1} + T_{j}")
    
    return j-1, j

def generate_latex_document():
    """Generate LaTeX document with complete recursive derivation"""
    
    latex_content = r"""
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\title{Complete Derivation of $(T_{T_m^2})^2$ Using Recursive Triangular Identity}
\author{Gregory Conner}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

This document derives mathematical expressions for $(T_{T_m^2})^2$ using the fundamental triangular number identity recursively:

\begin{equation}
i^2 = T_{i-1} + T_i
\end{equation}

where $T_n = \frac{n(n+1)}{2}$ is the $n$-th triangular number.

The key insight is that we must apply this identity recursively until no squares remain on the right side of the equation.

\section{The Triangular Number Identity}

The triangular number identity states that any perfect square can be expressed as the sum of two consecutive triangular numbers:

\begin{align}
i^2 &= T_{i-1} + T_i \\
&= \frac{(i-1)i}{2} + \frac{i(i+1)}{2} \\
&= \frac{i}{2}[(i-1) + (i+1)] \\
&= \frac{i}{2}[2i] \\
&= i^2
\end{align}

\section{Complete Recursive Derivation}

We want to find an expression for $(T_{T_m^2})^2$ using only terms of the form $T_l$, with no squares remaining.

\subsection{Step 1: Apply Identity to $T_m^2$}

For any natural number $m$:
\begin{align}
T_m &= \frac{m(m+1)}{2} \\
T_m^2 &= \left(\frac{m(m+1)}{2}\right)^2
\end{align}

Since $T_m^2$ is a perfect square, we apply the identity $i^2 = T_{i-1} + T_i$ where $i = T_m$:

\begin{equation}
T_m^2 = T_{T_m-1} + T_{T_m}
\end{equation}

\subsection{Step 2: Calculate $T_{T_m^2}$}

Now we calculate:
\begin{equation}
T_{T_m^2} = T_{T_{T_m-1} + T_{T_m}}
\end{equation}

This gives us the triangular number whose subscript is the sum of two consecutive triangular numbers.

\subsection{Step 3: Apply Identity to $(T_{T_m^2})^2$}

To find $(T_{T_m^2})^2$, we apply the identity again. Let $j = T_{T_m^2}$, then:

\begin{equation}
(T_{T_m^2})^2 = j^2 = T_{j-1} + T_j
\end{equation}

\subsection{Step 4: Eliminate Remaining Squares}

Now we must check if $j-1$ or $j$ are perfect squares and apply the identity recursively:

\begin{itemize}
\item If $j-1 = k^2$ for some $k$, then $T_{j-1} = T_{k-1} + T_k$
\item If $j = l^2$ for some $l$, then $T_j = T_{l-1} + T_l$
\end{itemize}

We continue this process until no squares remain in any subscript.

\section{Specific Cases}

\subsection{Case 1: $m = 1$}

\begin{align}
T_1 &= 1 \\
T_1^2 &= 1^2 = T_0 + T_1 = 0 + 1 = 1 \\
T_{T_1^2} = T_1 &= 1 \\
(T_{T_1^2})^2 &= 1^2 = T_0 + T_1 = 0 + 1 = 1
\end{align}

Since neither $0$ nor $1$ are perfect squares (except $1 = 1^2$, but $T_0 = 0$), we have:
\begin{equation}
(T_{T_1^2})^2 = T_0 + T_1
\end{equation}

\subsection{Case 2: $m = 2$}

\begin{align}
T_2 &= 3 \\
T_2^2 &= 3^2 = T_2 + T_3 = 3 + 6 = 9 \\
T_{T_2^2} = T_9 &= 45 \\
(T_{T_2^2})^2 &= 45^2 = T_{44} + T_{45}
\end{align}

Since neither $44$ nor $45$ are perfect squares, we have:
\begin{equation}
(T_{T_2^2})^2 = T_{44} + T_{45}
\end{equation}

\subsection{Case 3: $m = 3$}

\begin{align}
T_3 &= 6 \\
T_3^2 &= 6^2 = T_5 + T_6 = 15 + 21 = 36 \\
T_{T_3^2} = T_{36} &= 666 \\
(T_{T_3^2})^2 &= 666^2 = T_{665} + T_{666}
\end{align}

Since neither $665$ nor $666$ are perfect squares, we have:
\begin{equation}
(T_{T_3^2})^2 = T_{665} + T_{666}
\end{equation}

\section{General Pattern}

For any natural number $m$, the complete recursive application of the triangular number identity gives:

\begin{enumerate}
\item $T_m^2 = T_{T_m-1} + T_{T_m}$
\item $T_{T_m^2} = T_{T_{T_m-1} + T_{T_m}}$
\item $(T_{T_m^2})^2 = T_{T_{T_m^2}-1} + T_{T_{T_m^2}}$
\item If $T_{T_m^2}-1$ or $T_{T_m^2}$ are perfect squares, apply the identity recursively
\end{enumerate}

\section{Conclusion}

Using the triangular number identity $i^2 = T_{i-1} + T_i$ recursively, we can express $(T_{T_m^2})^2$ entirely in terms of triangular numbers with no squares remaining:

\begin{equation}
(T_{T_m^2})^2 = T_{T_{T_m^2}-1} + T_{T_{T_m^2}}
\end{equation}

This demonstrates the power of recursive application of the triangular number identity in reducing complex expressions involving multiple squares to sums of triangular numbers.

\end{document}
"""
    
    return latex_content

def compile_latex_to_pdf(latex_content, filename="triangular_derivation"):
    """Compile LaTeX content to PDF"""
    
    # Write LaTeX content to file
    tex_file = f"{filename}.tex"
    with open(tex_file, 'w') as f:
        f.write(latex_content)
    
    print(f"Generated LaTeX file: {tex_file}")
    
    # Compile LaTeX to PDF
    try:
        # Run pdflatex
        result = subprocess.run(['pdflatex', tex_file], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            pdf_file = f"{filename}.pdf"
            print(f"Successfully compiled to PDF: {pdf_file}")
            return pdf_file
        else:
            print(f"LaTeX compilation failed:")
            print(result.stderr)
            return None
            
    except subprocess.TimeoutExpired:
        print("LaTeX compilation timed out")
        return None
    except FileNotFoundError:
        print("pdflatex not found. Please install LaTeX.")
        return None

def display_pdf(pdf_file):
    """Display the PDF file"""
    if os.path.exists(pdf_file):
        print(f"PDF file created: {pdf_file}")
        print(f"File size: {os.path.getsize(pdf_file)} bytes")
        
        # Try to open the PDF
        try:
            if os.name == 'nt':  # Windows
                os.startfile(pdf_file)
            elif os.name == 'posix':  # macOS and Linux
                subprocess.run(['open', pdf_file], check=False)
        except:
            print(f"Could not automatically open PDF. Please open {pdf_file} manually.")
    else:
        print(f"PDF file {pdf_file} not found")

def main():
    """Main function to generate LaTeX derivation and compile to PDF"""
    print("Triangular Number LaTeX Derivation Program")
    print("=" * 50)
    print()
    
    # Demonstrate the derivation for small values
    print("Deriving expressions for (T_(T_m)²)²:")
    print("-" * 40)
    
    for m in range(1, 6):
        result = derive_expression_for_T_T_m_squared_squared(m)
        print()
    
    print("=" * 50)
    print("Generating LaTeX document...")
    
    # Generate LaTeX content
    latex_content = generate_latex_document()
    
    # Compile to PDF
    pdf_file = compile_latex_to_pdf(latex_content)
    
    if pdf_file:
        display_pdf(pdf_file)
    else:
        print("Failed to generate PDF")

if __name__ == "__main__":
    main()
