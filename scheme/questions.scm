(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  'replace-this-line)

(define (zip pairs)
  'replace-this-line)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define make_enumerate 
    (lambda (s i)
      (cond 
        ((null? s) nil)
        (else (cons (list i (car s)) (make_enumerate (cdr s) (+ i 1))))
      )
    )
  )
  (make_enumerate s 0)
)
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (define cons-all 
    (lambda (first rests) (
      map (lambda (lst) (
        append (list first) lst
      )) rests
    ))
  )
  (if (= total 0) 
      (list (list))
      (if (>= total (car denoms))
          (if
            (null? (cdr denoms))
              (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
              (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms)))
          )
          (if
            (null? (cdr denoms))
              (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
              (list-change total (cdr denoms))
          )
        ))
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           'replace-this-line
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         'replace-this-line
         ; END PROBLEM 19
         )))
