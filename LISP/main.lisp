; This is a comment


#|
This is for longer comments
#|


#|
SETQ - Assigns a value to a variable
Creating a variable using SETQ
The first argument is the name of the variable
The second argument is the value of the variable
#|
(setq my-name "Derek")
(setq pi 3.14)
(setq my-age 41)


#|
DEFVAR - Creates a global variable
Creating a global variable using DEFVAR
The first argument is the name of the variable
The second argument is the value of the variable
#|
(defvar my-last-name "Banas")
(defvar *e* 2.71)


#|
defparameter - Creates a global variable
Creating a global variable using defparameter
The first argument is the name of the variable
The second argument is the value of the variable
#|
(defparameter my-age 42)
(defparameter *e* 2.718)


#|
Function
(defun function-name (arguments)
  "Optional documentation"
  (body))

(defun - Creates a function
function-name - Name of the function
arguments - Arguments passed to the function
Optional documentation - Documentation for the function
body - The code the function executes
#|

; define a function that returns the area of a circle
(defun area (r)
  "Calculates the area of a circle with radius R"
  (* pi r r))

(area 3) ; calling area function with argument 3 which returns 28.26


#|
Introduction to Lists in LISP
Lists are a collection of atoms or other lists
Lists are surrounded by parentheses
Lists can be empty or contain items
Lists can contain any number of items
Lists can contain any type of data
#|
; create a list
'(1 2 3 4 5)

; create a list with a list inside
'(1 2 3 (4 5))

; create a list with a list inside
'(1 2 3 (4 5) 6)

; (6 (4 5) 3 2 1)

; List Functions
; car - Returns the first item in a list
(car '(1 2 3 4 5)) ; returns 1

; cdr - Returns everything but the first item in a list
(cdr '(1 2 3 4 5)) ; returns (2 3 4 5)

; cons - Adds an item to the front of a list
(cons 1 '(2 3 4 5)) ; returns (1 2 3 4 5)

; append - Adds an item to the end of a list
(append '(1 2 3 4 5) '(6 7 8 9 10)) ; returns (1 2 3 4 5 6 7 8 9 10)

; reverse - Reverses the order of a list
(reverse '(1 2 3 4 5)) ; returns (5 4 3 2 1)
