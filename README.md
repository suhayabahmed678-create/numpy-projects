# numpy-projects
Smart Matrix Toolkit is a command-line based matrix calculator that helps users perform fundamental linear algebra operations quickly and interactively.

Users can input matrices directly through the terminal and compute results such as:

Matrix addition
Matrix multiplication
Transpose
Determinant
Inverse
Matrix rank

The program automatically validates matrix shapes before performing operations and handles invalid operations safely.

This project demonstrates practical applications of the academic field Linear Algebra using Python.

Features

 Interactive CLI matrix input
 Matrix addition
 Matrix multiplication
 Matrix transpose
 Determinant calculation
 Matrix inverse calculation
 Matrix rank detection
 Shape validation before operations
 Clean class-based architecture
 Built using NumPy for efficient computation

Architecture

The project follows a simple modular design.

User Input (CLI)
        │
        ▼
MatrixBuilder
        │
        ▼
MatrixBrain  → matrix analysis
        │
        ▼
MatrixOps    → matrix operations
Components

MatrixBuilder

Handles matrix input
Converts user input into NumPy arrays

MatrixBrain

Performs matrix analysis:
transpose
determinant
inverse
rank

MatrixOps

Handles matrix-to-matrix operations:
addition
multiplication
