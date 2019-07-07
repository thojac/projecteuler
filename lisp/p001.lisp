;; Problem 1


;; Check if a number is multiple of x
(defun mul-of-x (num x)
  (if (= 0 (mod x num))
      T
      NIL
      ))

;; Check if n is multiples of 3 and 5
(defun multiple-of-sol (num)
  (OR
   (mul-of-x 3 num)
   (mul-of-x 5 num)))

;; Sum of all multiples of 3 or 5 below 1000
(defun solution (limit &optional (res 0))
  (cond ((= limit 1) res)
        ((multiple-of-sol limit) (solution (- limit 1) (+ limit res)))
        (T (solution (- limit 1) res))))
