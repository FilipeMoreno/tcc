class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Lidando com casos de borda
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determinando o sinal do quociente
        negative = (dividend < 0) != (divisor < 0)

        # Convertendo para valores absolutos
        dividend, divisor = abs(dividend), abs(divisor)

        # Realizando subtrações sucessivas
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                quotient += i
                i <<= 1
                temp <<= 1

        # Retornando o quociente com o sinal correto
        return -quotient if negative else quotient