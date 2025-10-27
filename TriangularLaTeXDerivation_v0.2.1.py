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
    Derive expression for (T_(T_m)²)² using the triangular number identity.
    
    Key insight: i² = T_{i-1} + T_i
    
    For (T_(T_m)²)²:
    1. T_m = m(m+1)/2
    2. T_m² = (T_m)² = T_{T_m-1} + T_{T_m} (applying the identity)
    3. T_(T_m²) = T_{T_{T_m-1} + T_{T_m}}
    4. (T_(T_m²))² = (T_{T_m²})² = T_{T_{T_m²}-1} + T_{T_{T_m²}} (applying the identity again)
    """
    T_m = triangular_number(m)
    T_m_squared = T_m * T_m
    T_of_T_m_squared = triangular_number(T_m_squared)
    
    print(f"Derivation for m = {m}:")
    print(f"T_{m} = {T_m}")
    print(f"T_{m}² = {T_m_squared}")
    
    # Find which consecutive triangular numbers sum to T_m²
    # We need T_{k-1} + T_k = T_m²
    # This means k² = T_m², so k = T_m
    k = T_m
    print(f"Applying identity: T_{m}² = T_{k-1} + T_{k}")
    print(f"T_{k-1} = {triangular_number(k-1)}")
    print(f"T_{k} = {triangular_number(k)}")
    print(f"Check: T_{k-1} + T_{k} = {triangular_number(k-1)} + {triangular_number(k)} = {triangular_number(k-1) + triangular_number(k)}")
    print(f"This equals T_{m}² = {T_m_squared} ✓")
    
    print(f"T_{T_m_squared} = {T_of_T_m_squared}")
    
    # Apply the identity to (T_{T_m²})²
    j = T_of_T_m_squared
    print(f"Applying identity: (T_{T_m_squared})² = T_{j-1} + T_{j}")
    print(f"T_{j-1} = {triangular_number(j-1)}")
    print(f"T_{j} = {triangular_number(j)}")
    print(f"Check: T_{j-1} + T_{j} = {triangular_number(j-1)} + {triangular_number(j)} = {triangular_number(j-1) + triangular_number(j)}")
    print(f"This equals (T_{T_m_squared})² = {T_of_T_m_squared ** 2} ✓")
    print(f"Final result: (T_{T_m_squared})² = T_{j-1} + T_{j}")
    
    return j-1, j

def generate_latex_document():
    """Generate LaTeX document with corrected mathematical derivation"""
    
    latex_content = r"""
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\title{Derivation of $(T_{T_m^2})^2$ Using Triangular Number Identity}
\author{Gregory Conner}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

This document derives mathematical expressions for $(T_{T_m^2})^2$ using the fundamental triangular number identity:

\begin{equation}
i^2 = T_{i-1} + T_i
\end{equation}

where $T_n = \frac{n(n+1)}{2}$ is the $n$-th triangular number.

\section{The Triangular Number Identity}

The key identity states that any perfect square can be expressed as the sum of two consecutive triangular numbers:

\begin{align}
i^2 &= T_{i-1} + T_i \\
&= \frac{(i-1)i}{2} + \frac{i(i+1)}{2} \\
&= \frac{i}{2}[(i-1) + (i+1)] \\
&= \frac{i}{2}[2i] \\
&= i^2
\end{align}

\section{Derivation of $(T_{T_m^2})^2$}

We want to find an expression for $(T_{T_m^2})^2$ using only terms of the form $T_l$.

\subsection{Step 1: Express $T_m$ and $T_m^2$}

For any natural number $m$:
\begin{align}
T_m &= \frac{m(m+1)}{2} \\
T_m^2 &= \left(\frac{m(m+1)}{2}\right)^2
\end{align}

\subsection{Step 2: Apply the identity to $T_m^2$}

Since $T_m^2$ is a perfect square, we can apply the identity $i^2 = T_{i-1} + T_i$:

Let $i = T_m$, then:
\begin{equation}
T_m^2 = T_{T_m-1} + T_{T_m}
\end{equation}

\subsection{Step 3: Calculate $T_{T_m^2}$}

Now we need to find $T_{T_m^2} = T_{T_{T_m-1} + T_{T_m}}$:

\begin{align}
T_{T_m^2} &= T_{T_{T_m-1} + T_{T_m}} \\
&= \frac{(T_{T_m-1} + T_{T_m})(T_{T_m-1} + T_{T_m} + 1)}{2}
\end{align}

\subsection{Step 4: Apply the identity to $(T_{T_m^2})^2$}

To find $(T_{T_m^2})^2$, we apply the identity again. Let $j = T_{T_m^2}$, then:

\begin{equation}
(T_{T_m^2})^2 = j^2 = T_{j-1} + T_j = T_{T_{T_m^2}-1} + T_{T_{T_m^2}}
\end{equation}

\section{Specific Cases}

\subsection{Case 1: $m = 1$}

\begin{align}
T_1 &= \frac{1 \cdot 2}{2} = 1 \\
T_1^2 &= 1^2 = T_0 + T_1 = 0 + 1 = 1 \\
T_{T_1^2} = T_1 &= 1 \\
(T_{T_1^2})^2 &= 1^2 = T_0 + T_1 = 0 + 1 = 1
\end{align}

Therefore: $(T_{T_1^2})^2 = T_0 + T_1$

\subsection{Case 2: $m = 2$}

\begin{align}
T_2 &= \frac{2 \cdot 3}{2} = 3 \\
T_2^2 &= 3^2 = T_2 + T_3 = 3 + 6 = 9 \\
T_{T_2^2} = T_9 &= \frac{9 \cdot 10}{2} = 45 \\
(T_{T_2^2})^2 &= 45^2 = T_{44} + T_{45}
\end{align}

Therefore: $(T_{T_2^2})^2 = T_{44} + T_{45}$

\subsection{Case 3: $m = 3$}

\begin{align}
T_3 &= \frac{3 \cdot 4}{2} = 6 \\
T_3^2 &= 6^2 = T_5 + T_6 = 15 + 21 = 36 \\
T_{T_3^2} = T_{36} &= \frac{36 \cdot 37}{2} = 666 \\
(T_{T_3^2})^2 &= 666^2 = T_{665} + T_{666}
\end{align}

Therefore: $(T_{T_3^2})^2 = T_{665} + T_{666}$

\section{General Pattern}

For any natural number $m$:

\begin{enumerate}
\item $T_m^2 = T_{T_m-1} + T_{T_m}$
\item $T_{T_m^2} = T_{T_{T_m-1} + T_{T_m}}$
\item $(T_{T_m^2})^2 = T_{T_{T_m^2}-1} + T_{T_{T_m^2}}$
\end{enumerate}

\section{Conclusion}

Using the triangular number identity $i^2 = T_{i-1} + T_i$, we can express $(T_{T_m^2})^2$ entirely in terms of triangular numbers:

\begin{equation}
(T_{T_m^2})^2 = T_{T_{T_m^2}-1} + T_{T_{T_m^2}}
\end{equation}

This demonstrates the power of the triangular number identity in reducing complex expressions involving squares to sums of triangular numbers.

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
