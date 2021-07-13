#! usr/bin/python3

# get the start fraction
numerator = int(input('What is the numerator? '))
denominator = int(input('\nWhat is the denominator? '))

# work out the common divisors for the numerator and denominator
common_divisors = [x for x in range(1, numerator+1) if numerator%x==0 and denominator%x==0]

# find the greatest common divisor
gcd = max(common_divisors)

# create the simplified fraction
simplified_numerator = numerator // gcd
simplified_denominator = denominator // gcd

# let the user know the most simple form of their fraction
print('\nThe most simple version of your fraction is: {} / {}'.format(simplified_numerator,
                                                                      simplified_denominator))
input('\nPress enter to exit...')
