# Day 63: argparse for my practice

import argparse

my_parser = argparse.ArgumentParser(description="My CLI tool")
my_parser.add_argument("name", help="My name argument")
my_parser.add_argument("--age", type=int, help="My age option")
my_parser.add_argument("--verbose", action="store_true", help="My verbose flag")

print("My parser configured")

my_parser2 = argparse.ArgumentParser()
my_parser2.add_argument("-f", "--file", required=True, help="My input file")
my_parser2.add_argument("-o", "--output", default="out.txt", help="My output file")

print("My file parser configured")

my_parser3 = argparse.ArgumentParser()
my_parser3.add_argument("--mode", choices=["dev", "prod"], default="dev")
my_parser3.add_argument("--count", type=int, default=1)

print("My choices parser configured")

my_parser4 = argparse.ArgumentParser()
my_parser4.add_argument("files", nargs="+", help="My input files")

print("My nargs parser configured")

my_parser5 = argparse.ArgumentParser()
my_subparsers = my_parser5.add_subparsers(dest="command")
my_add = my_subparsers.add_parser("add", help="My add command")
my_add.add_argument("numbers", nargs="+", type=int)
my_remove = my_subparsers.add_parser("remove", help="My remove command")
my_remove.add_argument("item", help="My item to remove")

print("My subcommands configured")

my_parser6 = argparse.ArgumentParser()
my_parser6.add_argument("--debug", action="store_true")
my_parser6.add_argument("--log-level", default="INFO")

print("My debug parser configured")

my_test_args = ["David", "--age", "30", "--verbose"]
my_namespace = my_parser.parse_args(my_test_args)
print(f"My parsed: name={my_namespace.name}, age={my_namespace.age}, verbose={my_namespace.verbose}")

my_parser7 = argparse.ArgumentParser()
my_parser7.add_argument("--config", type=argparse.FileType("r"))
print("My file type parser configured")

# Progress: part 4/4
