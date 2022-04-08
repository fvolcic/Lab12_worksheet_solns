; Write your definition of my-or here
(define-syntax my-or
  (syntax-rules ()
    ((my-or) #f)
    ((my-or arg0 args ...)
       (let ((value arg0))
         (if value
             value
             (my-or args ...)
         )
       )
    )
  )
)
