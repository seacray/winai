financial_products = {'k_fit_s': 8, 'k_fim_m': 5.5, 'k_fit_l': 7, 'k_fit_xl': 8.5}


def calculate_monthly_payment(pv: int, fv: int, annual_interest_rate: int, years: int):
    '''
    annual_interest_rate: the whole integer number i.e. 3, 5, 7, 9
    '''
    monthly_interest_rate = annual_interest_rate / 12 / 100

    total_months = years * 12
    if monthly_interest_rate > 0:
        monthly_payment = (pv * monthly_interest_rate + fv * monthly_interest_rate /
                           ((1 + monthly_interest_rate) ** total_months - 1)) / (1 - (1 + monthly_interest_rate) ** -
                                                                                 total_months)
    else:  # If the interest rate is 0
        monthly_payment = (pv - fv) / total_months

    return monthly_payment


def main(pv, fv, year):
    for k, v in financial_products.items():
        pmt = calculate_monthly_payment(pv, fv, annual_interest_rate=v, years=year)
        print(f'Your lovely product that suit for you {k}, with return={v}%, payment per month={pmt}')


if __name__ == '__main__':
    pv = 5000
    fv = 80000
    year = 10
    main(pv, fv, year)
