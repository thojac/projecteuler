;;;; Problem 2

(defun fib-even-sum
    (limit &optional (n1 1) (n2 1) (res 0))
  (if (> n1 limit)
      res
      (fib-even-sum limit n2 (+ n1 n2)
           (if (= 0 (mod n1 2))
               (+ res n1)
               res))))


