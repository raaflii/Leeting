function powerOfThree (n) {
    if (n  === 0) {
        return false;
    }

    if (n === 1) {
        return true;
    }

    while (true) {
        if (n % 3 === 0) {
            n /= 3;
            if (n === 1) {
                break;
            }
        } else {
            return false;
        }
    }

    return true;
}

a = powerOfThree (3)
print(a)