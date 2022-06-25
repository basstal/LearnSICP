from concurrent.futures import Executor
import os
import shutil
import sys
from pyutils.executor import Executor
import pyutils.fsext as fs
import pyutils.simplelogger as logger

sub_project = {
    "hog": [
        "-q 01",
        "-q 02 -u",
        "-q 02",
        "-q 03 -u",
        "-q 03",
        "-q 04 -u",
        "-q 04",
        "-q 05 -u",
        "-q 05",
        "-q 06 -u",
        "-q 06",
        "-q 07",
        "-q 08 -u",
        "-q 08",
        "-q 09 -u",
        "-q 09",
        "-q 10 -u",
        "-q 10",
        "-q 11 -u",
        "-q 11",
        "-q 12",
    ],
    "hw01": [""],
    "hw02": ["-q product", "-q factorial", "-q make_adder"],
    "hw03": [
        "-q has_seven",
        "-q summation",
        "-q accumulate",
        "-q summation_using_accumulate",
        "-q product_using_accumulate",
        "-q filtered_accumulate",
        "-q make_repeater",
        "-q church_to_int",
        "-q add_church",
        "-q mul_church",
        "-q pow_church",
    ],
    "hw04": [
        "-q taxicab",
        "-q squares",
        "-q g",
        "-q g_iter",
        "-q pingpong",
        "-q count_change",
        "-q make_anonymous_factorial",
    ],
    "lab00": [""],
    "lab01": [""],
    "lab02": [
        "-q lambda -u",
        "-q hof -u",
        "-q lambda_curry2",
        "-q composite_identity",
        "-q count_cond",
        "-q cycle",
    ],
    "lab03": [
        "-q gcd",
        "-q hailstone",
        "-q call_expressions -u",
        "-q cycle",
        "-q is_palindrome",
        "-q skip_mul_ok -u",
        "-q skip_mul",
        "-q is_prime",
        "-q interleaved_sum",
        "-q ten_pairs",
    ],
    "lab04": [
        "-q indexing -u",
        "-q lists -u",
        "-q if_this_not_that",
        "-q distance",
        "-q closer_city",
        "-q distance -q closer_city",
        "-q flatten",
        "-q merge",
        "-q create_row",
        "-q create_board",
        "-q replace_elem",
        "-q get_piece -q put_piece",
        "-q make_move",
        "-q print_board",
        "-q check_win_row",
        "-q check_win_column",
        "-q check_win",
    ],
    "maps": ["-u"],
}
only_lastest = True

if __name__ == "__main__":
    proj = sys.argv[1]
    if proj not in sub_project.keys():
        logger.error(f"{proj} not in {sub_project.keys()}")
        exit()
    current_dir = os.path.dirname(__file__)
    proj_dir = os.path.join(current_dir, proj)
    if not os.path.exists(os.path.join(proj_dir, "ok")):
        raw_path = "/".join(proj_dir.split(os.path.sep)[:2])
        ok_exe_pattern = os.path.join(raw_path, "**/ok")
        ok_exe = fs.search(ok_exe_pattern)
        assert ok_exe
        shutil.copyfile(ok_exe, os.path.join(proj_dir, "ok"))
    e = Executor()
    questions = sub_project[proj]
    for q in questions:
        if not only_lastest or q == questions[-1]:
            logger.info(f"current action : {q}")
            e.execute_file(
                "py", ["ok", "--local", q], work_dir=proj_dir, use_direct_stdout=True
            )
