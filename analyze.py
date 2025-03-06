from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    num_str = str(n)
    length = len(num_str)
    return n == sum(int(digit) ** length for digit in num_str)

def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syms[i]
            n -= val[i]
        i += 1
    return roman_num

def number_to_words(n):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return units[int(n)] if n < 10 else "Number too large for this example"

def analyze_number(number):
    number = float(number)
    return {
        "number": number,
        "even_odd": "Even" if number % 2 == 0 else "Odd",
        "prime": is_prime(int(number)),
        "armstrong": is_armstrong(int(number)),
        "integer": number == int(number),
        "rational_irrational": "Rational" if number == int(number) else "Irrational",
        "square": number ** 2,
        "cube": number ** 3,
        "roman": to_roman(int(number)),
        "words": number_to_words(number),
        "binary": bin(int(number)),
        "exponents": f"2^{number} = {2 ** number}, 10^{number} = {10 ** number}",
        "divisible_by": [i for i in range(1, int(number) + 1) if number % i == 0],
        "table": [f"{number} x {i} = {number * i}" for i in range(1, 11)],
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    number = data["number"]
    result = analyze_number(number)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
