from typing import Any

from sympy.printing.printer import Printer, print_function

class StrPrinter(Printer):
    printmethod = ...
    _default_settings: dict[str, Any] = ...
    _relationals: dict[str, str] = ...
    def parenthesize(self, item, level, strict=...) -> str: ...
    def stringify(self, args, sep, level=...): ...
    def emptyPrinter(self, expr) -> str: ...

    _print_MatrixSymbol = ...
    _print_RandomSymbol = ...

@print_function(StrPrinter)
def sstr(expr, **settings) -> str: ...

class StrReprPrinter(StrPrinter): ...

@print_function(StrReprPrinter)
def sstrrepr(expr, **settings) -> str: ...
