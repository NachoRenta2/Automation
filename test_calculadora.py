import pytest
from calculadora import suma, resta, division, multiplicar

@pytest.mark.parametrize("a,b,resultado", {# utilizamos las pruebas, pero mandandoles varios casos de una vez
    (10,5,15), 
    (-6,3,-3),
    (2,4,6)

})
def test_suma(a,b,resultado): #carga de pruebas de a 1.
    assert suma(a,b) == resultado

#@pytest.mark.manejoError con esa etiqueta generamos un grupo, q por ahora solo tiene zerodivision
def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        division(10,0)
        #puedo agregar nombres particulares para agrupar tests
#@pytest.mark.skip al momento de ejecutar, la salta por decision nuestra
#@pytest.merk.skip(reason="todavia no implementada") puedo darle una razon para el salto
def test_resta():
    assert resta(2,3) == -1

def test_division_decimal():
    assert division (10,3) == pytest.approx(3.333, rel=1e-3)
    #usamos una valor por aproximación para darlo por valido
@pytest.fixture
def numeros():
    return [1,2,3]
def test_suma(numeros):
    assert sum(numeros) == 6 #genero un paquete de numeros para ir probando los tests, o en diferentes test.