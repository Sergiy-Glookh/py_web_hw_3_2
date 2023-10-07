# Factorization Homework
This Python code demonstrates factorizing numbers using synchronous and parallel approaches.

## Usage
To run the code:

```
python main.py
```
It will factorize some sample numbers both synchronously and in parallel using multiple processes.

The results are validated against expected outputs.

## Functions
- `get_divisors` - Get all divisors of a number
- `factorize_sync` - Factorize numbers synchronously
- `factorize_parallel` - Factorize numbers in parallel

## Explanation
This homework shows how to factorize numbers in Python.

The synchronous version uses a simple loop.

The parallel version uses the multiprocessing module to split the work across multiple processes.

The results are validated to ensure correct output.