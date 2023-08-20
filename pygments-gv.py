from pathlib import Path
from pygments import highlight
from pygments.style import Style
from pygments.lexers import Python3Lexer
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic
from pygments.formatters import HtmlFormatter

# Define custom style
class MyStyle(Style):
    styles = {
        Comment:                'italic #9E9E9E',
        Comment.Preproc:        '#9E9E9E',
        Keyword:                'bold #2494BF',
        # Keyword.Constant:       'bold #64B5F6',
        # Keyword.Namespace:      'bold #283593',
        Name.Variable:          '#D81B60',
        Name.Class:             'bold #800080',
        Name.Function:          '#800080',
        Name.Builtin:           '#3949AB',
        String:                 '#009688',
        String.Doc:             'italic #9E9E9E',
        # Operator:               'bold',
        Operator.Word:          'bold #00897B',
    }

cwd = Path.cwd()
formatter = HtmlFormatter(style=MyStyle, full=True, cssfile=cwd.joinpath('gv_pygments.css'))

# The following creates some dummy html code but more importantly also writes
# the css file.
code = 'print("Hello World")'
result = highlight(code, Python3Lexer(), formatter)
print(result)
