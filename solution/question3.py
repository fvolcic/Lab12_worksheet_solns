
def gen_predicate(seq):
    """Generate a c*r type checking predicate of arbitrary length.

    Requires that seq is at least of length 2 and contains only a's and d's.
    >>> gen_predicate('dda')
    '(lambda (x) (and (pair? x) (pair? (car x)) (pair? (cdar x))))'
    >>> gen_predicate('ada')
    '(lambda (x) (and (pair? x) (pair? (car x)) (pair? (cdar x))))'
    >>> gen_predicate('aaaa')
    '(lambda (x) (and (pair? x) (pair? (car x)) (pair? (caar x)) (pair? (caaar x))))'
    """
    def helper(seq):
        if len(seq) == 1:
            return '(pair? x)'
        return helper(seq[1:]) + f' (pair? (c{seq[1:]}r x))'

    return f'(lambda (x) (and {helper(seq)}))'
