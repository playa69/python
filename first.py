# optimized (complexity: O(const)) 
n = 1_000_000_002 

sum3 = ((3 + n)*n//3)//2 #arithmetic summary
max7 = 999_999_987 # precalculated
max4 = 999_999_984 # precalculated

i = max7 - 27
i = i//30 + 1
j = max4 - 24
j = j//30 + 1

sum_7 = ((27 + 999_999_987)*i)//2 #arithmetic summary
sum_4 = ((24 + 999_999_984)*j)//2 #arithmetic summary

final = sum3 - (sum_7+sum_4) # final equation


#long
#sum([i for i in range(1, 1_000_000_003, 3) if i%10!=4 and i%10!=7])

#133333334466666672

def arithmetic_series_sum(first_: int,  last_: int, n_: int) -> int:
    """Арифметическая прогрессия от first_ до last_ c колличеством элеме n_."""
    return n_ * (first_ + last_) // 2
 
 
def get_max_count(max_number: int, period: int, first_occurred_num: int) -> int:
    """Максимальное колличество чисел вида first_occurred_num + period * N в max_number."""
    return (max_number - first_occurred_num) // period
 
 
def sum_periodic_numbers(max_number: int, period: int, first_occurred_num: int) -> int:
    """Сумма всех чисел вида first_occurred_num + period * N, не превышающих max_number."""
    _max_count = get_max_count(max_number, period, first_occurred_num)
    return (_max_count + 1) * first_occurred_num + period * arithmetic_series_sum(1, _max_count, _max_count)
 
 
if __name__ == "__main__":
    max_number = 1_000_000_002
    # Сумма всех чисел, делящихся на 3
    max_count = max_number // 3
    s_1 = arithmetic_series_sum(3, max_count * 3, max_count)
    # Пусть есть множество чисел, кратных 3 => {3, 6, 9, ...}
    # Множество остатков от деления на 10 является конечным
    # Период повторения остатков равен 30
    # Значит все числа, оканчивающиеся на 7 и 4 имеют вид
    # 24 + 30 * N и 27 + 30 * N соответственно
 
    # Сумма всех чисел, кратных 3, оканчивающихся на 4
    s_2 = sum_periodic_numbers(max_number, 30, 24)
    # Сумма всех чисел, кратных 3, оканчивающихся на 7
    s_3 = sum_periodic_numbers(max_number, 30, 27)
 
    print(s_1 - s_2 - s_3)




    