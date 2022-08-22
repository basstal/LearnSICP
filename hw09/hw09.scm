(define (how-many-dots s)
  (if (or (null? s) (number? s)) 0 
    (if (and (not (pair? (cdr s))) (number? (cdr s))) (+ 1 (how-many-dots (cdr s)) (how-many-dots (car s))) (+ (how-many-dots (cdr s)) (how-many-dots (car s))))
  )
)

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (cadr expr) var) (derive (caddr expr) var))
)

(define (derive-product expr var)
  (make-sum (make-product (derive (cadr expr) var) (caddr expr) ) (make-product (derive (caddr expr) var) (cadr expr) ))
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond 
        ((=number? exponent 1) base)
        ((=number? exponent 0) 1)
        ((and (number? base) (number? exponent)) (expt base exponent))
        (else (list '^ base exponent)))
)

(define (base exp)
  (cadr exp)
)

(define (exponent exp)
  (caddr exp)
)

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  ;TODO Extensions: There are many ways to extend this symbolic differentiation system. For example, you could simplify nested exponentiation expression such as (^ (^ x 3) 2), products of exponents such as (* (^ x 2) (^ x 3)), and sums of products such as (+ (* 2 x) (* 3 x)). You could apply the chain rule when deriving exponents, so that expressions like (derive '(^ (^ x y) 3) 'x) are handled correctly. Enjoy!
  (define (calc) (make-product (exponent exp) (make-exp var (- (exponent exp) 1))))
  (cond ((number? (base exp)) 0)
        ((variable? (base exp)) (if (same-variable? (base exp) var)
          (calc) 'Error
        ))
        ((sum? (base exp)) (make-product (calc) (derive-sum (base exp) var)))
        ((product? (base exp)) (print 'TODO))
        ((exp? (base exp)) 
          (derive-exp (make-exp (base (base exp)) (make-product (exponent exp) (exponent (base exp)))) var))
        (else 'Error))
)
