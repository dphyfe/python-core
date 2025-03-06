# Day 63: argparse for my practice

import argparse

my_parser = argparse.ArgumentParser(description="My CLI tool")
my_parser.add_argument("name", help="My name argument")
my_parser.add_argument("--age", type=int, help="My age option")
my_parser.add_argument("--verbose", action="store_true", help="My verbose flag")

print("My parser configured")

my_parser2 = argparse.ArgumentParser()
my_parser2.add_argument("-f", "--file", required=True, help="My input file")
