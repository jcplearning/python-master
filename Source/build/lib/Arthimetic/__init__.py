# Init program for Arthimetic module

from .Add_Sub import add, sub
from .Mul_Div import mul, div
import logging

def main():
    logging.basicConfig(level=logging.INFO,filemode="w", filename="arthimetic.log", format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Addition: %s", add(10, 5))
    logging.info("Subtraction: %s", sub(10, 5))
    logging.info("Multiplication: %s", mul(10, 5))
    logging.info("Division: %s", div(10, 5))

    
    
