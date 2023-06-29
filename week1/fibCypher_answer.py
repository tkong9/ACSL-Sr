"""
Fibonacci Cypher

Name: <your name>
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Complete the 'fibCypher' function below. #
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. CHARACTER option
# 2. INTEGER num1
# 3. INTEGER num2
# 4. CHARACTER key
# 5. STRING msg #
def fibCypher(option, num1, num2, key, msg):
    # hints: use the alphabet list below
    #        use the ord() and chr() functions
    #        use ASCII arithmetic
    final = ""
    fibSequence = [num1, num2]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # Write your code here

    for _ in msg:
        next_fib = fibSequence[-2] + fibSequence[-1]
        fibSequence.append(next_fib)

    if option == "E":
        for i, c in enumerate(msg, start=0):
            if i % 2 == 0:
                newOffsetIndex = (alphabet.index(key) + fibSequence[i]) % 26
                final += str(ord(c) + (3 * ord(alphabet[newOffsetIndex]))) + " "
            else:
                newOffsetIndex = (alphabet.index(key) - fibSequence[i]) % 26
                final += str(ord(c) + (3 * ord(alphabet[newOffsetIndex]))) + " "
        return final
    else:
        decodeList = msg.split()
        for i, num in enumerate(decodeList, start=0):
            if i % 2 == 0:
                newOffsetIndex = (alphabet.index(key) + fibSequence[i]) % 26
                decodedChar = chr(int(num) - (3 * ord(alphabet[newOffsetIndex])))
                final += decodedChar
            else:
                newOffsetIndex = (alphabet.index(key) - fibSequence[i]) % 26
                decodedChar = chr(int(num) - (3 * ord(alphabet[newOffsetIndex])))
                final += decodedChar
        return final


def testFibCypher():
    print('Testing fibCypher()...', end='')
    assert fibCypher('E', 1, 2, 'a', 'Fibonacci cyphers are fun to encode and decode.').strip() == '364 468 398 465 425 427 453 444 405 368 432 415 442 437 467 450 436 338 403 405 407 386 423 441 476 359 446 477 365 425 410 414 465 430 416 338 397 407 394 326 391 395 465 408 460 407 391'
    assert fibCypher('D', 4, 7, 'x', '383 450 432 338 400 394 475 335 444 440 471 448 350 408 424 443 359 364 355 388 371 332 383 448 436 412 407 344 430 449 454 377 371 457 431 407 405 401 395 471 467 323 420 400 426 443 452 459 448 436 419 419 403').strip() == 'You may only use C++, Java, and Python in HackerRank.'
    assert fibCypher('D', 7, 10, 'p', '434 403 409 430 421 401 323 397 342 466 392 398 463 403 424 359 429 454 353 465 413 410 362 426 453 332 425 431 419 377 418 405 466 473 362 462 414 427 430 444 434 377 427 463 471 444 470 415 417 459 400 416 427 385').strip() == 'Madam, I\'m Adam is one of the most common palindromes.'
    assert fibCypher('E', 16, 9, 'l', 'What happens when the first number is greater than the second?').strip() == "381 401 418 416 377 461 409 403 457 449 431 466 326 422 419 413 437 341 458 395 398 350 405 444 480 412 431 338 443 414 469 437 446 432 383 396 421 341 424 426 434 400 470 452 441 380 419 395 433 467 335 416 431 398 386 460 434 435 432 449 406 420"
    assert fibCypher('D', 11, 13, 'q', '378 404 434 338 480 454 464 453 450 380 441 459 344 356 377 397 406 439 409 459 392 440 416 323 418 465 425 405 404 436 393 405 432 350 458 426 409 446 392 432 427 377 411 410 377 410 416 422 362 445 440 443 465 422 476 393 434 332 391 457 478 432 420 445 399 413 431 433 383 422 410 440 338 365 462 468 430 392 410 362 419 477 475 431 395 414 377 338 478 461 453 392 371 467 434 462 411 410 377 405 421 365 409 472 403 444 411 411 394 392 376 340 348 388 350 352 373 364').strip() == 'The ratio of 2 adjacent Fibonacci numbers in the sequence approaches the Golden number, phi, which is approx. 1.618...'
    print('Passed!')


if __name__ == '__main__':
    testFibCypher()
