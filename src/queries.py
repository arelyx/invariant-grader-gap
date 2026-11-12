"""Turn (program, loop marker, candidate invariant) into the C files the graders check.

Uses Wonda's AstProgram so the instrumentation is identical to the Wonda/InvBench protocol:
  correctness query: assert(candidate) at the loop head, nothing assumed
  sufficiency query: assume(candidate) at the loop head, assert the program's original target
"""
import paths  # noqa: F401  (puts the Wonda clone on sys.path)
from pycparser import c_parser
from wonda.core.ast_program import AstProgram
from wonda.core.property import Property


def build_program(program_text: str) -> AstProgram:
    prog = AstProgram().from_code(program_text)
    prog.process(print_ast=False)
    return prog


def check_syntax(invariant_text: str) -> bool:
    try:
        c_parser.CParser().parse(f"int __f(void) {{ return ({invariant_text}); }}")
        return True
    except Exception:
        return False


def correctness_query(prog: AstProgram, marker: str, invariant_text: str) -> str:
    cand = Property(content=invariant_text, marker_name=marker)
    return prog.get_program_with_assertion(property_to_assert=cand, assumptions=[], for_llm=False)


def sufficiency_query(prog: AstProgram, marker: str, invariant_text: str) -> str:
    cand = Property(content=invariant_text, marker_name=marker)
    return prog.get_program_with_assertion(property_to_assert=prog.get_target_assert(),
                                           assumptions=[cand], for_llm=False)
