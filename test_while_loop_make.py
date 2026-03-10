import re
import sys
import random
import builtins
from io import StringIO

filename = "while_loop_make"


def run_program(inputs, rand_sequence):
    """Helper: runs the student module with given inputs and fixed random, returns output."""
    sys.modules.pop(filename, None)
    original_input = builtins.input
    original_randint = random.randint
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    builtins.input = lambda _: inputs.pop(0)
    random.randint = lambda a, b: rand_sequence.pop(0)
    try:
        __import__(filename)
        return sys.stdout.getvalue()
    finally:
        builtins.input = original_input
        random.randint = original_randint
        sys.stdout = original_stdout
        sys.modules.pop(filename, None)


def test_header_comments():
    with open(f"{filename}.py", encoding="utf-8") as f:
        kids_code = f.read()

    docstring_match = re.search(r'^\s*"""(.*?)"""', kids_code, re.DOTALL)
    assert docstring_match is not None, "You must include a header docstring using triple quotes (\"\"\")"
    docstring = docstring_match.group(1)

    author_match = re.search(r'author\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert author_match and author_match.group(1).strip(), "Your header must include a non-empty 'author:' field"

    date_match = re.search(r'date\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert date_match and date_match.group(1).strip(), "Your header must include a non-empty 'date:' field"

    non_field_lines = [
        l.strip() for l in docstring.strip().splitlines()
        if l.strip()
        and not re.match(r'(author|date)\s*:', l.strip(), re.IGNORECASE)
    ]
    assert len(non_field_lines) >= 1, "Your header must include a short description of the program"


def test_all_combos():
    """Test all 9 win/loss/tie combos, invalid input handling, and final counters"""
    # Each round: (player_move, rand_val, expected_output_snippet)
    combos = [
        ("rock",     1, "It's a tie!"),
        ("rock",     2, "You lose! paper covers rock"),
        ("rock",     3, "You win! rock smashes scissors"),
        ("paper",    1, "You win! paper covers rock"),
        ("paper",    2, "It's a tie!"),
        ("paper",    3, "You lose! scissors cuts paper"),
        ("scissors", 1, "You lose! rock smashes scissors"),
        ("scissors", 2, "You win! scissors cuts paper"),
        ("scissors", 3, "It's a tie!"),
    ]

    for move, rand_val, expected in combos:
        out = run_program(["play", move, "quit"], [rand_val])
        assert expected in out, f"For {move} vs computer (rand={rand_val}): expected '{expected}'"


def test_invalid_move():
    """Invalid move should print 'Invalid move!' then accept valid move"""
    out = run_program(["play", "ROCKSSS", "rock", "quit"], [3])
    assert "Invalid move!" in out, "Expected 'Invalid move!' for bad input"
    assert "You win! rock smashes scissors" in out, "Expected valid move accepted after invalid"


def test_counters():
    """Win, loss, tie, and quit-immediately counters should all work"""
    # quit immediately -> all zeros
    out = run_program(["quit"], [])
    assert "Number of wins: 0" in out and "Number of losses: 0" in out and "Number of ties: 0" in out, \
        "Expected all counters to be 0 when quitting immediately"

    # 1 win (rock vs scissors), 1 loss (paper vs scissors), 1 tie (rock vs rock)
    out = run_program(["play", "rock", "play", "paper", "play", "rock", "quit"], [3, 3, 1])
    assert "Number of wins: 1" in out, "Expected 1 win"
    assert "Number of losses: 1" in out, "Expected 1 loss"
    assert "Number of ties: 1" in out, "Expected 1 tie"