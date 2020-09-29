def bmi(mass, height):
    """Вычисляет индекс массы тела по введенным массе и росту человека"""
    return (mass/((height/100)**2))

man_mass, man_height = map(float, input('Введите свою массу(кг) и рост(см): ').split( ))
BMI = bmi(man_mass, man_height)

if BMI < 16:
    print('Выраженный дефицит массы')
elif 16 <= BMI <18.5:
    print('Недостаточная масса тела')
elif 18.5 <= BMI < 25:
    print('Нормальная масса')
elif 25 <= BMI < 30:
    print('Избыточная масса')
elif 30 <= BMI < 35:
    print('Ожирение первой степени')
elif 35 <= BMI < 40:
    print('Ожирение второй степени')
elif BMI >= 40:
    print('Ожирение третьей степени')
