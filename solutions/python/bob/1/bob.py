def response(hey_bob):
    if len(hey_bob) == 0 or len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    elif hey_bob.strip()[-1] == "?" and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and not (hey_bob[-1] == "?"):
        return "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"

    else:
        return "Whatever."