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
    Derive expression for (T_(T_m)²)² using the consecutive sum property.
    
    Key insight: T_n + T_(n+1) = (n+1)²
    
    For (T_(T_m)²)²:
    1. T_m = m(m+1)/2
    2. T_m² = (m(m+1)/2)² = m²(m+1)²/4
    3. T_(T_m²) = T_m²(T_m² + 1)/2
    4. (T_(T_m²))² = (T_m²(T_m² + 1)/2)²
    
    Now, if T_(T_m²) = k² for some k, then:
    T_(T_m²) = T_(k-1) + T_k = k²
    So (T_(T_m²))² = (k²)² = k⁴
    """
    T_m = triangular_number(m)
    T_m_squared = T_m * T_m
    T_of_T_m_squared = triangular_number(T_m_squared)
    
    print(f"Derivation for m = {m}:")
    print(f"T_{m} = {T_m}")
    print(f"T_{m}² = {T_m_squared}")
    print(f"T_{T_m_squared} = {T_of_T_m_squared}")
    print(f"(T_{T_m_squared})² = {T_of_T_m_squared ** 2}")
    
    # Check if we can use consecutive sum property
    if is_perfect_square(T_of_T_m_squared):
        sqrt_val = int(math.sqrt(T_of_T_m_squared))
        print(f"Since T_{T_m_squared} = {T_of_T_m_squared} = {sqrt_val}²,")
        print(f"we have T_{T_m_squared} = T_{sqrt_val-1} + T_{sqrt_val}")
        print(f"Therefore: (T_{T_m_squared})² = ({sqrt_val}²)² = {sqrt_val}⁴")
        return sqrt_val, True
    else:
        print(f"T_{T_m_squared} = {T_of_T_m_squared} is not a perfect square")
        print("Cannot directly apply consecutive sum property")
        return None, False

def generate_latex_document():
    """Generate LaTeX document with mathematical derivation"""
    
    latex_content = r"""
\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\title{Derivation of $(T_{T_m^2})^2$ Using Consecutive Triangular Sum Property}
\author{Gregory Conner}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

This document derives mathematical expressions for $(T_{T_m^2})^2$ using the fundamental property of triangular numbers:

\begin{equation}
T_n + T_{n+1} = (n+1)^2
\end{equation}

where $T_n = \frac{n(n+1)}{2}$ is the $n$-th triangular number.

\section{The Consecutive Triangular Sum Property}

The consecutive triangular sum property states that the sum of two consecutive triangular numbers equals the square of the larger subscript:

\begin{align}
T_n + T_{n+1} &= \frac{n(n+1)}{2} + \frac{(n+1)(n+2)}{2} \\
&= \frac{(n+1)}{2}[n + (n+2)] \\
&= \frac{(n+1)}{2}[2n+2] \\
&= \frac{(n+1)}{2} \cdot 2(n+1) \\
&= (n+1)^2
\end{align}

\section{Derivation of $(T_{T_m^2})^2$}

We want to find an expression for $(T_{T_m^2})^2$ using the consecutive sum property.

\subsection{Step 1: Express $T_m$ and $T_m^2$}

For any natural number $m$:
\begin{align}
T_m &= \frac{m(m+1)}{2} \\
T_m^2 &= \left(\frac{m(m+1)}{2}\right)^2 = \frac{m^2(m+1)^2}{4}
\end{align}

\subsection{Step 2: Calculate $T_{T_m^2}$}

\begin{align}
T_{T_m^2} &= \frac{T_m^2(T_m^2 + 1)}{2} \\
&= \frac{\frac{m^2(m+1)^2}{4}\left(\frac{m^2(m+1)^2}{4} + 1\right)}{2} \\
&= \frac{m^2(m+1)^2}{8}\left(\frac{m^2(m+1)^2}{4} + 1\right) \\
&= \frac{m^2(m+1)^2}{8} \cdot \frac{m^2(m+1)^2 + 4}{4} \\
&= \frac{m^2(m+1)^2[m^2(m+1)^2 + 4]}{32}
\end{align}

\subsection{Step 3: Apply Consecutive Sum Property}

If $T_{T_m^2}$ is a perfect square, say $T_{T_m^2} = k^2$ for some $k$, then we can apply the consecutive sum property:

\begin{equation}
T_{T_m^2} = T_{k-1} + T_k = k^2
\end{equation}

Therefore:
\begin{equation}
(T_{T_m^2})^2 = (k^2)^2 = k^4
\end{equation}

\subsection{Step 4: General Expression}

For the general case, we have:
\begin{equation}
(T_{T_m^2})^2 = \left(\frac{m^2(m+1)^2[m^2(m+1)^2 + 4]}{32}\right)^2
\end{equation}

\section{Specific Cases}

\subsection{Case 1: $m = 1$}

\begin{align}
T_1 &= \frac{1 \cdot 2}{2} = 1 \\
T_1^2 &= 1 \\
T_{T_1^2} = T_1 &= 1 = 1^2
\end{align}

Since $T_1 = 1^2$, we can apply the consecutive sum property:
\begin{align}
T_1 &= T_0 + T_1 = 0 + 1 = 1 \\
(T_{T_1^2})^2 &= (T_1)^2 = (1^2)^2 = 1^4 = 1
\end{align}

\subsection{Case 2: $m = 2$}

\begin{align}
T_2 &= \frac{2 \cdot 3}{2} = 3 \\
T_2^2 &= 9 \\
T_{T_2^2} = T_9 &= \frac{9 \cdot 10}{2} = 45
\end{align}

Since $T_9 = 45$ is not a perfect square, we cannot directly apply the consecutive sum property. The general formula gives:
\begin{equation}
(T_{T_2^2})^2 = (T_9)^2 = 45^2 = 2025
\end{equation}

\section{Conclusion}

The consecutive triangular sum property $T_n + T_{n+1} = (n+1)^2$ provides a powerful tool for deriving expressions involving triangular numbers. For $(T_{T_m^2})^2$:

\begin{itemize}
\item When $T_{T_m^2}$ is a perfect square, we can express $(T_{T_m^2})^2$ as $k^4$ where $k^2 = T_{T_m^2}$
\item In the general case, we have the explicit formula involving $m^2(m+1)^2$
\item The case $m = 1$ is special, allowing direct application of the consecutive sum property
\end{itemize}

This derivation demonstrates the deep connections between triangular numbers and perfect squares, revealing the elegant mathematical structure underlying these sequences.

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
