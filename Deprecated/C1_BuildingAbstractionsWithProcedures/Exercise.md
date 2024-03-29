- [Exercise 1.1](#exercise-11)
- [Exercise 1.2](#exercise-12)
- [Exercise 1.3](#exercise-13)
  - [Answer 1.3](#answer-13)
- [Exercise 1.4](#exercise-14)
- [Exercise 1.5](#exercise-15)
  - [Answer 1.5](#answer-15)
- [Exercise 1.6](#exercise-16)
  - [Answer 1.6](#answer-16)
- [Exercise 1.7](#exercise-17)
  - [Answer 1.7](#answer-17)
- [Exercise 1.8](#exercise-18)
  - [Answer 1.8](#answer-18)
- [Exercise 1.9](#exercise-19)
- [Exercise 1.10](#exercise-110)
  - [Answer 1.10](#answer-110)
- [Exercise 1.11](#exercise-111)
  - [Answer 1.11](#answer-111)
- [Exercise 1.12](#exercise-112)
  - [Answer 1.12](#answer-112)
- [Exercise 1.13](#exercise-113)
- [Exercise 1.14](#exercise-114)
  - [Answer 1.14](#answer-114)
- [Exercise 1.15](#exercise-115)
  - [Answer 1.15](#answer-115)
- [Exercise 1.16](#exercise-116)
  - [Answer 1.16](#answer-116)
- [Exercise 1.17](#exercise-117)
  - [Answer 1.17](#answer-117)
- [Exercise 1.18](#exercise-118)
  - [Answer 1.18](#answer-118)
- [Exercise 1.19](#exercise-119)
- [Exercise 1.20](#exercise-120)
  - [Answer 1.20](#answer-120)
- [Exercise 1.21](#exercise-121)
  - [Answer 1.21](#answer-121)
- [Exercise 1.22](#exercise-122)
  - [Answer 1.22](#answer-122)
- [Exercise 1.23](#exercise-123)
  - [Answer 1.23](#answer-123)
- [Exercise 1.24](#exercise-124)
- [Exercise 1.25](#exercise-125)
- [Exercise 1.26](#exercise-126)
- [Exercise 1.27](#exercise-127)
- [Exercise 1.28](#exercise-128)
- [Exercise 1.29](#exercise-129)
  - [Answer 1.29](#answer-129)
- [Exercise 1.30](#exercise-130)
  - [Answer 1.30](#answer-130)
- [Exercise 1.31](#exercise-131)
  - [Answer 1.31](#answer-131)
- [Exercise 1.32](#exercise-132)
  - [Answer 1.32](#answer-132)
- [Exercise 1.33](#exercise-133)
  - [Answer 1.33](#answer-133)
- [Exercise 1.34](#exercise-134)
  - [Answer 1.34](#answer-134)
- [Exercise 1.35](#exercise-135)
  - [Answer 1.35](#answer-135)
- [Exercise 1.36](#exercise-136)
  - [Answer 1.36](#answer-136)
- [Exercise 1.37](#exercise-137)
  - [Answer 1.37](#answer-137)
- [Exercise 1.38](#exercise-138)
  - [Answer 1.38](#answer-138)
- [Exercise 1.39](#exercise-139)
  - [Answer 1.39](#answer-139)
- [Exercise 1.40](#exercise-140)
  - [Answer 1.40](#answer-140)
- [Exercise 1.41](#exercise-141)
  - [Answer 1.41](#answer-141)
- [Exercise 1.42](#exercise-142)
  - [Answer 1.42](#answer-142)
- [Exercise 1.43](#exercise-143)
  - [Answer 1.43](#answer-143)
- [Exercise 1.44](#exercise-144)
  - [Answer 1.44](#answer-144)
- [Exercise 1.45](#exercise-145)
- [Exercise 1.46](#exercise-146)
# Exercise 1.1

Below is a sequence of expressions. What is the result printed by the interpreter in response to each expression?Assume that the sequence is to be evaluated in the order in which it is presented.

# Exercise 1.2

Translate the following expression into prefix form:

# Exercise 1.3

Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.

## Answer 1.3
```python
def sum_squares_larger(a, b, c):
    if a < b and a < c:
        return b * b + c * c
    elif b < a and b < c:
        return a * a + c * c
    else:
        return a * a + b * b
```

# Exercise 1.4

Observe that our model of evaluation allows for combinations whose operators are compound expres-sions. Use this observation to describe the behavior of the following procedure:

# Exercise 1.5

Ben Bitdiddle has invented a test to determine whether the interpreter he is faced with is using applicative-order evaluation or normal-order evaluation. He deﬁnes the following two procedures:

```scheme
(define (p) (p))
(define (test x y)
    (if (= x 0) 0 y))

(test 0 (p))
```

Then he evaluates the expression

What behavior will Ben observe with an interpreter that uses applicative-order evaluation? What behavior will he observe with an interpreter that uses normal-order evaluation? Explain your answer. (Assume that the evaluation rule for the special form if is the same whether the interpreter is using normal or applicative order: The predicate expression is evaluated ﬁrst, and the result determines whether to evaluate the consequent or the alternative expression.)

## Answer 1.5

```python
def p(p):
    return p

def test(x, y):
    if x == 0:
        return 0
    else:
        return y

test(0, p)
```

normal-order will infinitely expanding p.

# Exercise 1.6

Alyssa P. Hacker doesn’t see why if needs to be provided as a special form. “Why can’t I just define it as an ordinary procedure in terms of cond?” she asks. Alyssa’s friend Eva Lu Ator claims this can indeed be done, and she defines a new version of if:

```scheme
(define (new-if predicate then-clause else-clause)
    (cond (predicate then-clause)
        (else else-clause)))
```

Eva demonstrates the program for Alyssa:

```scheme
(new-if (= 2 3) 0 5)
5
(new-if (= 1 1) 0 5)
0
```

Delighted, Alyssa uses new-if to rewrite the square-root program:

```scheme
(define (sqrt-iter guess x)
    (new-if (good-enough? guess x)
        guess
        (sqrt-iter (improve guess x) x)))
```

What happens when Alyssa attempts to use this to compute square roots? Explain.

## Answer 1.6

[Scripts/newtons_method_square.py](Scripts/newtons_method_square.py)

# Exercise 1.7

The good-enough? test used in computing square roots will not be very eﬀective for ﬁnding the square roots of very small numbers. Also, in real computers, arith-metic operations are almost always performed with lim-ited precision. This makes our test inadequate for very large numbers. Explain these statements, with examples showing how the test fails for small and large numbers. An alterna-tive strategy for implementing good-enough? is to watch how guess changes from one iteration to the next and to stop when the change is a very small fraction of the guess. Design a square-root procedure that uses this kind of end test. Does this work better for small and large numbers?

## Answer 1.7

[Scripts/newtons_method_square.py](Scripts/newtons_method_square.py)

# Exercise 1.8

Newton’s method for cube roots is based on the fact that if y is an approximation to the cube root of x, then a better approximation is given by the value

$$\frac{{x}/{y}^2 + 2y}{3}$$

Use this formula to implement a cube-root procedure analogous to the square-root procedure. (In Section 1.3.4 we will see how to implement Newton’s method in general as an abstraction of these square-root and cube-root procedures.)


## Answer 1.8

[Scripts/cube_root.py](Scripts/cube_root.py)

# Exercise 1.9

Each of the following two procedures deﬁnes a method for adding two positive integers in terms of the procedures inc, which increments its argument by 1, and dec, which decrements its argument by 1.

```scheme
(define (+ a b)
    (if (= a 0) b (inc (+ (dec a) b))))
(define (+ a b)
    (if (= a 0) b (+ (dec a) (inc b))))
```

Using the substitution model, illustrate the process generated by each procedure in evaluating (+ 4 5). Are these processes iterative or recursive?

# Exercise 1.10

The following procedure computes a math-ematical function called Ackermann’s function.


```scheme
(define (A x y)
    (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1) (A x (- y 1))))))
```

What are the values of the following expressions?

```scheme
(A 1 10)
(A 2 4)
(A 3 3)
```

Consider the following procedures, where A is the procedure defined above:

```scheme
(define (f n) (A 0 n))
(define (g n) (A 1 n))
(define (h n) (A 2 n))
(define (k n) (* 5 n n))
```

Give concise mathematical definitions for the functions computed by the procedures f, g, and h for positive integer values of n. For example, (k n) computes 5n2.

## Answer 1.10

[Scripts/ackermann_func.py](Scripts/ackermann_func.py)

# Exercise 1.11

A function f is deﬁned by the rule that

$$f(n)=\begin{cases}
n & \text{if} & n < 3 \\
f(n-1)+2f(n-2)+3f(n-3) & \text{if} & n\geq{3}
\end{cases}$$

Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process.

## Answer 1.11

[Scripts/func_f.py](Scripts/func_f.py)


# Exercise 1.12

The following pattern of numbers is called Pascal’s triangle.

```
                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4       1
                ...
```

The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it. Write a procedure that computes elements of Pascal’s triangle by means of a recursive process.

## Answer 1.12

[Scripts/pascals_triangle.py](Scripts/pascals_triangle.py)


# Exercise 1.13

Prove that Fib(n) is the closest integer to $ϕ^n /\sqrt{5}$, where $ϕ = (1 + \sqrt{5})/2$. Hint: Let $ψ = (1 − \sqrt{5})/2$. Use induction and the deﬁnition of the Fibonacci numbers(see Section 1.2.2) to prove that $Fib(n) = (φ^n − ψ^n )/\sqrt{5}$

# Exercise 1.14

Draw the tree illustrating the process generated by the count-change procedure of Section 1.2.2 in making change for 11 cents. What are the orders of growth of the space and number of steps used by this process as the amount to be changed increases?

## Answer 1.14

space $\theta{(1)}$ number of steps $\theta{(5^n)}$$

# Exercise 1.15

The sine of an angle (speciﬁed in radians) can be computed by making use of the approximation sin x ≈ x if x is suﬃciently small, and the trigonometric identity

$$\sin{x} = 3 \sin{\frac{x}{3}}- 4\sin^3{\frac{x}{3}}$$

to reduce the size of the argument of sin. (For purposes of this exercise an angle is considered "sufficiently small" if its magnitude is not greater than 0.1 radians.) These ideas are incorporated in the following procedures:

```scheme
(define (cube x) (* x x x))
(define (p x) (- (* 3 x) (* 4 (cube x))))
(define (sine angle)
    (if (not (> (abs angle) 0.1))
        angle
        (p (sine (/ angle 3.0)))))
```

a.	How many times is the procedure p applied when (sine 12.15) is evaluated?

b.	What is the order of growth in space and number of steps (as a function of a) used by the process generated by the sine procedure when (sine a) is evaluated?

## Answer 1.15

a. 2 times

b. space $\theta{(\log_3{n})}$ number of steps $\theta{(\log_3{n})}$

# Exercise 1.16

Design a procedure that evolves an iterative exponentiation process that uses successive squaring and uses a logarithmic number of steps, as does fast-expt.(Hint: Using the observation that $(b^{n/2})^2 = (b^2)^{n/2}$, keep, along with the exponent n and the base b, an additional state variable a, and define the state transformation in such a way that the product $ab^n$ is unchanged from state to state. At the beginning of the process a is taken to be 1, and the answer is given by the value of a at the end of the process. In general, the technique of defining an invariant quantity that remains unchanged from state to state is a powerful way to think about the design of iterative algorithms.)

## Answer 1.16

[Scripts/exp_iterative.py](Scripts/exp_iterative.py)

# Exercise 1.17

The exponentiation algorithms in this section are based on performing exponentiation by means of repeated multiplication. In a similar way, one can perform integer multiplication by means of repeated addition. The following multiplication procedure (in which it is assumed that our language can only add, not multiply) is analogous to the expt procedure:

```scheme
(define (* a b)
    (if (= b 0)
        0
        (+ a (* a (- b 1)))))
```

This algorithm takes a number of steps that is linear in b. Now suppose we include, together with addition, operations double, which doubles an integer, and halve, which divides an (even) integer by 2. Using these, design a multiplication procedure analogous to fast-expt that uses a logarithmic number of steps.


## Answer 1.17

[Scripts/mul.py](Scripts/mul.py)

# Exercise 1.18

Using the results of Exercise 1.16 and Exercise 1.17, devise a procedure that generates an iterative process for multiplying two integers in terms of adding, doubling, and halving and uses a logarithmic number of steps.

## Answer 1.18

[Scripts/mul_iterative.py](Scripts/mul_iterative.py)

# Exercise 1.19

There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps. Recall the transformation of the state variables a and b in the fib-iter process of Section 1.2.2: $a ← a +b$ and $b ← a$. Call this transformation T , and observe that applying T over and over again n times, starting with 1 and 0, produces the pair Fib(n + 1) and Fib(n). In other words, the Fibonacci numbers are produced by applying T n , the nth power of the transformationT , starting with the pair (1, 0). Now consider T to be the special case of p = 0 and q = 1 in a family of transformations Tpq , where Tpq transforms the pair (a, b) according to $a ← bq + aq + ap$ and $b ← bp + aq$. Show that if we apply such a transformation Tpq twice, the effect is the same as using a single transformation Tp′q′ of the same form, and compute p′ and q′ in terms of p and q. This gives us an explicit way to square these transformations, and thus we can compute T n using successive squaring, as in the fast-expt procedure. Put this all together to complete the following procedure, which runs in a logarithmic number of steps:

```scheme
(define (fib n)
    (fib-iter 1 0 0 1 n))

(define (fib-iter a b p q count)
    (cond ((= count 0) b)
        ((even? count)
        (fib-iter a 
                    b
                    ⟨??⟩ ; compute p′
                    ⟨??⟩ ; compute q′
                    (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q)) 
                        p
                        q
                        (- count 1)))))
```


# Exercise 1.20

The process that a procedure generates is of course dependent on the rules used by the interpreter. As an example, consider the iterative gcd procedure given above. Suppose we were to interpret this procedure using normal-order evaluation, as discussed in Section 1.1.5. (The normal-order-evaluation rule for if is described in Exercise 1.5.) Using the substitution method (for normal order), illus-trate the process generated in evaluating (gcd 206 40) and indicate the remainder operations that are actually per-formed. How many remainder operations are actually per-formed in the normal-order evaluation of (gcd 206 40)?In the applicative-order evaluation?

## Answer 1.20

4 times in normal-order evaluation, 4 times in applicative-order evaluation.

# Exercise 1.21

Use the smallest-divisor procedure to ﬁnd the smallest divisor of each of the following numbers: 199, 1999, 19999.

## Answer 1.21

[Scripts/smallest_divisor.py](Scripts/smallest_divisor.py)


# Exercise 1.22

Most Lisp implementations include a primitive called runtime that returns an integer that specifies the amount of time the system has been running (measured, for example, in microseconds). The following timed-prime-test procedure, when called with an integer n, prints n and checks to see if n is prime. If n is prime, the procedure prints three asterisks followed by the amount of time used in performing the test.

```scheme
(define (timed-prime-test n)
    (newline)
    (display n)
    (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
    (if (prime? n)
    (report-prime (- (runtime) start-time))))
(define (report-prime elapsed-time)
    (display " *** ")
    (display elapsed-time))
```

Using this procedure, write a procedure search-for-primes that checks the primality of consecutive odd integers in a specified range. Use your procedure to find the three smallest primes larger than 1000; larger than 10,000; larger than 100,000; larger than 1,000,000. Note the time needed to test each prime. Since the testing algorithm has order of growth of $\Theta({\sqrt{n}})$, you should expect that testing for primes around 10,000 should take about $\sqrt{10}$ times as long as testing for primes around 1000. Do your timing data bear this out? How well do the data for 100,000 and 1,000,000 support the $\Theta({\sqrt{n}})$ prediction? Is your result compatible with the notion that programs on your machine run in time proportional to the number of steps required for the computation?

## Answer 1.22

[Scripts/search_for_primes.py](Scripts/search_for_primes.py)

# Exercise 1.23

The smallest-divisor procedure shown at the start of this section does lots of needless testing: After it checks to see if the number is divisible by 2 there is no point in checking to see if it is divisible by any larger even numbers. This suggests that the values used for test-divisor should not be 2, 3, 4, 5, 6, . . ., but rather 2, 3, 5, 7, 9, . . .. To implement this change, define a procedure next that returns 3 if its input is equal to 2 and otherwise returns its input plus 2. Modify the smallest-divisor procedure to use (next test-divisor) instead of (+ test-divisor 1). With timed-prime-test incorporating this modified version of smallest-divisor, run the test for each of the 12 primes found in Exercise 1.22. Since this modification halves the number of test steps, you should expect it to run about twice as fast. Is this expectation confirmed? If not, what is the observed ratio of the speeds of the two algorithms, and how do you explain the fact that it is different from 2?


## Answer 1.23

[Scripts/smallest_divisor.py](Scripts/smallest_divisor.py)


# Exercise 1.24

Modify the timed-prime-test procedure of Exercise 1.22 to use fast-prime? (the Fermat method), and test each of the 12 primes you found in that exercise. Since the Fermat test has $\Theta({\log{n}})$ growth, how would you expect the time to test primes near 1,000,000 to compare with the time needed to test primes near 1000? Do your data bear this out? Can you explain any discrepancy you find?

[Scripts/search_for_primes.py](Scripts/search_for_primes.py)

# Exercise 1.25

Alyssa P. Hacker complains that we went to a lot of extra work in writing expmod. After all, she says, since we already know how to compute exponentials, we could have simply written

```scheme
(define (expmod base exp m)
    (remainder (fast-expt base exp) m))
```

Is she correct? Would this procedure serve as well for our fast prime tester? Explain.

# Exercise 1.26

Louis Reasoner is having great difficulty doing Exercise 1.24. His fast-prime? test seems to run more slowly than his prime? test. Louis calls his friend Eva Lu Ator over to help. When they examine Louis’s code, they find that he has rewritten the expmod procedure to use an explicit multiplication, rather than calling square:

```scheme
(define (expmod base exp m)
    (cond ((= exp 0) 1)
        ((even? exp)
        (remainder (* (expmod base (/ exp 2) m)
                        (expmod base (/ exp 2) m)) 
                    m))
        (else
            (remainder (* base
                            (expmod base (- exp 1) m)) 
                        m))))
```

“I don’t see what diffierence that could make,” says Louis. “I do.” says Eva. “By writing the procedure like that, you have transformed the $\Theta({\log{n}})$ process into a $\Theta({n})$ process.” Explain.

# Exercise 1.27

Demonstrate that the Carmichael numbers listed in Footnote 1.47 really do fool the Fermat test. That is, write a procedure that takes an integer n and tests whether an is congruent to a modulo n for every a < n, and try your procedure on the given Carmichael numbers.

# Exercise 1.28

One variant of the Fermat test that cannot be fooled is called the Miller-Rabin test (Miller 1976; Rabin 1980). This starts from an alternate form of Fermat’s Little Theorem, which states that if n is a prime number and a is any positive integer less than n, then a raised to the (n−1)-st power is congruent to 1 modulo n. To test the primality of a number n by the Miller-Rabin test, we pick a random number a < n and raise a to the (n − 1)-st power modulo n using the expmod procedure. However, whenever we perform the squaring step in expmod, we check to see if we have discovered a “nontrivial square root of 1 modulo n,” that is, a number not equal to 1 or n −1 whose square is equal to 1 modulo n. It is possible to prove that if such a nontrivial square root of 1 exists, then n is not prime. It is also possible to prove that if n is an odd number that is not prime, then, for at least half the numbers a < n, computing $a^{n−1}$ in this way will reveal a nontrivial square root of 1 modulo n. (This is why the Miller-Rabin test cannot be fooled.) Modify the expmod procedure to signal if it discovers a nontrivial square root of 1, and use this to implement the Miller-Rabin test with a procedure analogous to fermat-test. Check your procedure by testing various known primes and non-primes. Hint: One convenient way to make expmod signal is to have it return 0.

# Exercise 1.29

Simpson’s Rule is a more accurate method of numerical integration than the method illustrated above. Using Simpson’s Rule, the integral of a function f between a and b is approximated as

$$\frac{h}{3}(y_0+4y_1+2y_2+4y_3+2y_4+ ... + 2y_{n-2}+4y_{n-1}+y_n)$$

where h = (b − a)/n, for some even integer n, and $y_k = f (a + kh)$. (Increasing n increases the accuracy of the approximation.) Define a procedure that takes as arguments f , a, b, and n and returns the value of the integral, computed using Simpson’s Rule. Use your procedure to integrate cube between 0 and 1 (with n = 100 and n = 1000), and compare the results to those of the integral procedure shown above.

## Answer 1.29

[Scripts/simpson_rule.py](Scripts/simpson_rule.py)

# Exercise 1.30

The sum procedure above generates a linear recursion. The procedure can be rewritten so that the sum is performed iteratively. Show how to do this by filling in the missing expressions in the following definition:

```scheme
(define (sum term a next b)
    (define (iter a result)
        (if ⟨??⟩
            ⟨??⟩
            (iter ⟨??⟩ ⟨??⟩)))
(iter ⟨??⟩ ⟨??⟩))
```

## Answer 1.30

```scheme
(define (sum term a next b)
    (define (iter a result)
        (if (a > b)
            (result)
            (iter (next a) (+ result (term a)))))
    (iter a 0))
```

# Exercise 1.31

a. The sum procedure is only the simplest of a vast number of similar abstractions that can be captured as higherorder procedures. Write an analogous procedure called product that returns the product of the values of a function at points over a given range. Show how to define factorial in terms of product. Also use product to compute approximations to π using the formula

$$\frac{\pi}{4} = \frac{2 * 4 *4 * 6 * 6 * 8...}{3 * 3 * 5 * 5 * 7 * 7...}$$

b. If your product procedure generates a recursive process, write one that generates an iterative process. If it generates an iterative process, write one that generates a recursive process.

## Answer 1.31

ab. [Scripts/product.py](Scripts/product.py)


# Exercise 1.32

a. Show that sum and product (Exercise 1.31) are both special cases of a still more general notion called accumulate that combines a collection of terms, using some general accumulation function:

```scheme
(accumulate combiner null-value term a next b)
```

accumulate takes as arguments the same term and range specifications as sum and product, together with a combiner procedure (of two arguments) that specifies how the current term is to be combined with the accumulation of the preceding terms and a null-value that specifies what base value to use when the terms run out. Write accumulate and show how sum and product can both be defined as simple calls to accumulate.

b. If your accumulate procedure generates a recursive process, write one that generates an iterative process. If it generates an iterative process, write one that generates a recursive process.

## Answer 1.32

ab. [Scripts/accumulate.py](Scripts/accumulate.py)

# Exercise 1.33

You can obtain an even more general version of accumulate (Exercise 1.32) by introducing the notion of a filter on the terms to be combined. That is, combine only those terms derived from values in the range that satisfy a specified condition. The resulting filtered-accumulate abstraction takes the same arguments as accumulate, together with an additional predicate of one argument that specifies the filter. Write filtered-accumulate as a procedure. Show how to express the following using filtered-accumulate:

a.	the sum of the squares of the prime numbers in the interval a to b (assuming that you have a prime? predicate already written)

b.	the product of all the positive integers less than n that are relatively prime to n (i.e., all positive integers i < n such that GCD(i, n) = 1).

## Answer 1.33

[Scripts/filtered_accumulate.py](Scripts/filtered_accumulate.py)

# Exercise 1.34

Suppose we define the procedure

```scheme
(define (f g) (g 2))
```

Then we have

```scheme
(f square)
4
(f (lambda (z) (* z (+ z 1))))
6
```

What happens if we (perversely) ask the interpreter to evaluate the combination (f f)? Explain.

## Answer 1.34

expression will represent like (2 2) which make no sense.

# Exercise 1.35

Show that the golden ratio ϕ (Section 1.2.2) is a fixed point of the transformation $x \to{ 1 + 1/x}$, and use this fact to compute ϕ by means of the fixed-point procedure.

## Answer 1.35

[Scripts/golden_ratio.py](Scripts/golden_ratio.py)

# Exercise 1.36

Modify fixed-point so that it prints the sequence of approximations it generates, using the newline and display primitives shown in Exercise 1.22. Then find a solution to xx = 1000 by finding a fixed point of $x \to log(1000)/ log(x)$. (Use Scheme’s primitive log procedure, which computes natural logarithms.) Compare the number of steps this takes with and without average damping. (Note that you cannot start fixed-point with a guess of 1, as this would cause division by log(1) = 0.)

## Answer 1.36

[Scripts/fixed_point_average_damping.py](Scripts/fixed_point_average_damping.py)

# Exercise 1.37

a. An infinite continued fraction is an expression of the form
$$f = \frac{N_1}{D_1 + \frac{N_2}{D_2 + \frac{N_3}{D_3 + ...}}}$$

As an example, one can show that the infinite continued fraction expansion with the $N_i$ and the $D_i$ all equal to 1 produces 1/ϕ, where ϕ is the golden ratio (described in Section 1.2.2). One way to approximate an infinite continued fraction is to truncate the expansion after a given number of terms. Such a truncationa so-called k-term finite continued fraction—has the form

$$\frac{N_1}{D_1 + \frac{N_2}{... + \frac{N_k}{D_k}}}$$

Suppose that n and d are procedures of one argument (the term index i) that return the $N_i$ and $D_i$ of the terms of the continued fraction. Define a procedure cont-frac such that evaluating (cont-frac n d k) computes the value of the k-term finite continued fraction. Check your procedure by approximating 1/ϕ using

```scheme
(cont-frac (lambda (i) 1.0)
            (lambda (i) 1.0)
            k)
```

for successive values of k. How large must you make k in order to get an approximation that is accurate to 4 decimal places?

b. If your cont-frac procedure generates a recursive process, write one that generates an iterative process. If it generates an iterative process, write one that generates a recursive process.

## Answer 1.37

[Scripts/cont_frac_expression.py](Scripts/cont_frac_expression.py)

# Exercise 1.38

In 1737, the Swiss mathematician Leonhard Euler published a memoir De Fractionibus Continuis, which included a continued fraction expansion for e − 2, where e is the base of the natural logarithms. In this fraction, the $N_i$ are all 1, and the $D_i$ are successively 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, . . .. Write a program that uses your cont-frac procedure from Exercise 1.37 to approximate e, based on Euler’s expansion.

## Answer 1.38

[Scripts/cont_e.py](Scripts/cont_e.py)

# Exercise 1.39

A continued fraction representation of the tangent function was published in 1770 by the German mathematician J.H. Lambert:

$$\tan{x} =\frac{x}{1 - \frac{x^2}{3 - \frac{x^2}{5 - ...}}}$$

where x is in radians. Define a procedure (tan-cf x k) that computes an approximation to the tangent function based on Lambert’s formula. k specifies the number of terms to compute, as in Exercise 1.37.

## Answer 1.39

[Scripts/tan_cf.py](Scripts/tan_cf.py)

# Exercise 1.40

Define a procedure cubic that can be used together with the newtons-method procedure in expressions of the form

```scheme
(newtons-method (cubic a b c) 1)
```

to approximate zeros of the cubic $x^3 + ax^2 + bx + c$.

## Answer 1.40

[Scripts/cube_in_newtons_method.py](Scripts/cube_in_newtons_method.py)

# Exercise 1.41

Define a procedure double that takes a procedure of one argument as argument and returns a procedure that applies the original procedure twice. For example, if inc is a procedure that adds 1 to its argument, then (double inc) should be a procedure that adds 2. What value is returned by

```scheme
(((double (double double)) inc) 5)
```

## Answer 1.41

13 ( 5 + 8 )

# Exercise 1.42

Let $f$ and $g$ be two one-argument functions.The composition $f$ after $g$ is defined to be the function $x \to f (g(x))$. Define a procedure compose that implements composition. For example, if inc is a procedure that adds 1 to its argument,

```scheme
((compose square inc) 6)
49
```

## Answer 1.42

[Scripts/compose.py](Scripts/compose.py)

# Exercise 1.43

If f is a numerical function and n is a positive integer, then we can form the nth repeated application of f , which is defined to be the function whose value at x is $f (f (. . . (f (x)) . . . ))$. For example, if f is the function $x \to x + 1$, then the nth repeated application of f is the function $x \to x +n$. If f is the operation of squaring a number, then the nth repeated application of f is the function that raises its argument to the $2^n$-th power. Write a procedure that takes as inputs a procedure that computes f and a positive integer n and returns the procedure that computes the nth repeated application of f . Your procedure should be able to be used as follows:

```scheme
((repeated square 2) 5)
625
```

Hint: You may find it convenient to use compose from Exercise 1.42.

## Answer 1.43

[Scripts/repeated.py](Scripts/repeated.py)


# Exercise 1.44

The idea of smoothing a function is an important concept in signal processing. If f is a function and dx is some small number, then the smoothed version of f is the function whose value at a point x is the average of $f (x − dx)$, $f (x)$, and $f (x +dx)$. Write a procedure smooth that takes as input a procedure that computes f and returns a procedure that computes the smoothed f . It is sometimes valuable to repeatedly smooth a function (that is, smooth the smoothed function, and so on) to obtain the n-fold smoothed function. Show how to generate the n-fold smoothed function of any given function using smooth and repeated from Exercise 1.43.

## Answer 1.44

[Scripts/smoothing.py](Scripts/smoothing.py)

# Exercise 1.45

We saw in Section 1.3.3 that attempting to compute square roots by naively finding a fixed point of $y \to x/y$ does not converge, and that this can be fixed by average damping. The same method works for finding cube roots as fixed points of the average-damped $y \to x/y^2$. Unfortunately, the process does not work for fourth roots—a single average damp is not enough to make a fixed-point search for $y \to x/y^3$ converge. On the other hand, if we average damp twice (i.e., use the average damp of the average damp of $y \to x/y^3$) the fixed-point search does converge. Do some experiments to determine how many average damps are required to compute nth roots as a fixed-point search based upon repeated average damping of $y \to x/y^{n−1}$. Use this to implement a simple procedure for computing nth roots using fixed-point, average-damp, and the repeated procedure of Exercise 1.43. Assume that any arithmetic operations you need are available as primitives.

# Exercise 1.46

Several of the numerical methods described in this chapter are instances of an extremely general computational strategy known as iterative improvement. Iterative improvement says that, to compute something, we start with an initial guess for the answer, test if the guess is good enough, and otherwise improve the guess and continue the process using the improved guess as the new guess. Write a procedure iterative-improve that takes two procedures as arguments: a method for telling whether a guess is good enough and a method for improving a guess. iterative-improve should return as its value a procedure that takes a guess as argument and keeps improving the guess until it is good enough. Rewrite the sqrt procedure of Section 1.1.7 and the fixed-point procedure of Section 1.3.3 in terms of iterative-improve.