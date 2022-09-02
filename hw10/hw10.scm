(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (if (< start n) (combiner (term start) (accumulate combiner (+ start 1) n term)) (term start))
  )
)

(define (accumulate-tail combiner start n term)
  (define (accumulate-tail-impl combiner start n term result)
    (if (= start n)
        (combiner result (term start))
        (accumulate-tail-impl combiner (+ start 1) n term (combiner result (term start)))
    )
  )
  (accumulate-tail-impl combiner (+ start 1) n term (term start))
)

(define-macro (list-of expr for var in seq if filter-fn)
  'TODO
)