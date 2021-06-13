Prueba técnica Desarrollador Backend Python/Django

The live project is host at https://nestorbracho.dev in Amazon Web Services

Project Header

'
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'

Answer source code:

```python

def main():
    initial_number = 100
    percentage = 99  # target percentage
    bounce = 0  # Total bouncy numbers
    final_percentage = percentage / 100
    while True:
        aux_i = str(initial_number)
        aux_list = [int(j) for j in aux_i]
        is_bounce = False
        aux_bool = None
        for k in range(0, len(aux_list) - 1):
            if aux_list[k] > aux_list[k + 1]:
                if aux_bool is None:
                    aux_bool = True
                elif aux_bool is False:
                    is_bounce = True
                    break
            elif aux_list[k] < aux_list[k + 1]:
                if aux_bool is None:
                    aux_bool = False
                elif aux_bool is True:
                    is_bounce = True
                    break
        if is_bounce:
            bounce += 1
        if float(bounce) / float(initial_number) >= final_percentage:
            break
        initial_number += 1

    print('\n')
    print('final number: ', initial_number)
    print('bounce numbers: ', bounce)
    print('\n')


if __name__ == "__main__":
    main()
```