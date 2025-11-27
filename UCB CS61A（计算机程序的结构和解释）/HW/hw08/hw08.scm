(define (ascending? s) 
(if (equal? s '())
    #t
    (if (equal? (cdr s) '())
        #t
        (let
            (
                (x (car s))
                (y (car (cdr s)))
            )
            (if 
                (<= x y)
                (ascending? (cdr s))
                #f
            )
        )
    )
)
)

(define (my-filter pred s) 
    (if (null? s)
        nil
        (
            if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
    
)

(define (interleave lst1 lst2) 
(if (null? lst1 )
    lst2
    (if (null? lst2)
        lst1
        (let
            (
                (x (car lst1))
                (y (car lst2))
            )
            (cons x (cons y (interleave (cdr lst1) (cdr lst2))))
        )
    )
)
)

(define (no-repeats s) 
(if (null? s)
    nil
  (let 
    ((other (cons (car s) (my-filter (lambda (x) (not (= x (car s)))) (cdr s)))))
    (cons (car s) (no-repeats (cdr other)))
)
)
)


