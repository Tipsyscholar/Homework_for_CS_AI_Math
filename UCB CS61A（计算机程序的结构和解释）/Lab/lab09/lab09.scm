(define (over-or-under num1 num2) 
  (if (< num1 num2)
        -1
        (if (= num1 num2)
          0
          1
        )
  )
)

(define (make-adder num) 
  (lambda (n) (+ n num))
)

(define (composed f g) 
  (lambda (n) (f (g n)))
)

(define (repeat f n) 
  (if (= n 1)
      f
      (composed f (repeat f (- n 1)))
    )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (= b 0)
    a
    ;;(gcd  (min a b)  (modulo (max a b) (min a b)))
    (gcd b (modulo a b))
  )

)
