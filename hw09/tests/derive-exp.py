test = {
  'name': 'derive-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (derive (make-exp x^3 2) 'x)
          (* 6 (^ x 5))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (derive x^2 'x) ; Remember products have the form (* a b)
          (* 2 x)
          scm> (derive x^3 'x)
          (* 3 (^ x 2))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (derive (make-sum x^3 x^2) 'x)
          (+ (* 3 (^ x 2)) (* 2 x))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw09)
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      scm> (define x^y (make-exp 'x 'y))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
