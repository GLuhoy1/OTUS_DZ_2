import pytest
from src import Triangle, Rectangle, Square, Circle


@pytest.fixture(params=[
    {
        'class': Rectangle,
        'args': (4, 5),
        'expected_perimeter': 18,
        'expected_area': 20
    },
    {
        'class': Circle,
        'args': (3,),
        'expected_perimeter': 18.85,
        'expected_area': 28.27
    },
    {
        'class': Square,
        'args': (5,),
        'expected_perimeter': 20,
        'expected_area': 25
    },
    {
        'class': Triangle,
        'args': (3, 4, 5),
        'expected_perimeter': 12,
        'expected_area': 6
    },
], ids=["Rectangle", "Circle", "Square", "Triangle"])
def figure_fixture(request):
    data = request.param
    figure_class = data['class']
    args = data['args']
    expected_perimeter = data['expected_perimeter']
    expected_area = data['expected_area']
    figure = figure_class(*args)
    figure.expected_perimeter = expected_perimeter
    figure.expected_area = expected_area
    return figure


@pytest.mark.parametrize('figure_class, args', [
    (Rectangle, (-5, 5)),
    (Circle, ('abc',)),
    (Square, (-5,)),
    (Triangle, (1, 2, 10)), ])
def test_invalid_parameters(figure_class, args):
    pytest.raises((TypeError, ValueError), figure_class, *args)


def test_instance_creation(figure_fixture):
    figure = figure_fixture
    assert isinstance(figure, (Rectangle, Circle, Square, Triangle))


def test_instance_name_attribute(figure_fixture):
    assert hasattr(figure_fixture, 'name')


def test_perimeter_calculation(figure_fixture):
    figure = figure_fixture
    expected_perimeter = round(figure_fixture.expected_perimeter, 2)
    calculated_perimeter = figure.perimeter
    assert calculated_perimeter == expected_perimeter


def test_area_calculation(figure_fixture):
    figure = figure_fixture
    expected_area = round(figure_fixture.expected_area, 2)
    calculated_area = figure.area
    assert calculated_area == expected_area


'''Приношу извинения за обращение через коментарий внутри кода, но не нашёл способ использовать разные фигуры 
для проверки следующих двух функций(хотя подозреваю это далеко не единственная моя ошибка)
Если сможете подсказть способ проверки без создания дополнительной фикстуры-буду крайне признателен.
При этом если я правильно понимаю, то сам факт и коректность работы функций:
add_area и add_perimeter
эти тесты проверяют'''


def test_add_area_calculation(figure_fixture):
    figure = figure_fixture
    expected_value = round((figure_fixture.expected_area + figure_fixture.expected_area), 2)
    calculated_add_area = figure.add_area(figure)
    assert expected_value == calculated_add_area


def test_add_perimeter_calculation(figure_fixture):
    figure = figure_fixture
    expected_value = round((figure_fixture.expected_perimeter + figure_fixture.expected_perimeter), 2)
    calculated_add_perimeter = figure.add_perimeter(figure)
    assert expected_value == calculated_add_perimeter
