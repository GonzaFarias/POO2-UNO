package practica;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class testRobot {

	@Test
	public void creoRobotTest() {
		int a[] = { 5, 4 };
		int b[] = { 10, 10 };

		@SuppressWarnings("unused")
		Robot r = new Robot(a, Sentido.NORTE, new Cuadricula(b));
	}

	@Test
	public void creoCuadriculaTest() {

		int b[] = { 10, 10 };
		@SuppressWarnings("unused")
		Cuadricula c = new Cuadricula(b);
	}

	@Test
	public void avanzarRobotTest() {

		int a[] = { 5, 4 };
		int b[] = { 10, 10 };

		Robot r = new Robot(a, Sentido.NORTE, new Cuadricula(b));

		r.instruccion("A", 3);
		int esperado = 7;
		int obtenido = r.getPosicionFila();

		assertEquals(esperado, obtenido, 0.1);

	}

	@Test
	public void RobotLlegaLimiteXTest() {

		int a[] = { 5, 4 };
		int b[] = { 10, 10 };

		Robot r = new Robot(a, Sentido.NORTE, new Cuadricula(b));

		r.instruccion("A", 15);
		int esperado = 10;
		int obtenido = r.getPosicionFila();

		assertEquals(esperado, obtenido, 0.1);

	}

	@Test
	public void RobotLlegaLimiteYTest() {

		int a[] = { 5, 4 };
		int b[] = { 10, 10 };

		Robot r = new Robot(a, Sentido.OESTE, new Cuadricula(b));

		r.instruccion("A", 15);
		int esperado = 10;
		int obtenido = r.getPosicionColumna();

		assertEquals(esperado, obtenido, 0.1);

	}

	@Test
	public void RobotRotaTest() {

		int a[] = { 5, 4 };
		int b[] = { 10, 10 };

		Robot r = new Robot(a, Sentido.OESTE, new Cuadricula(b));

		r.instruccion("R", 1);
		Sentido esperado = Sentido.NORTE;
		Sentido obtenido = r.getSentido();
		assertTrue(esperado.equals(obtenido));

		r.instruccion("R", 2);
		esperado = Sentido.SUR;
		obtenido = r.getSentido();
		assertTrue(esperado.equals(obtenido));

		r.instruccion("R", 1);
		esperado = Sentido.OESTE;
		obtenido = r.getSentido();
		assertTrue(esperado.equals(obtenido));

		r.instruccion("R", 2);
		esperado = Sentido.ESTE;
		obtenido = r.getSentido();
		assertTrue(esperado.equals(obtenido));

	}

	@Test(expected = Exception.class)
	public void creoCuadriculaMayorCienTest() {

		int b[] = { 101, 10 };
		@SuppressWarnings("unused")
		Cuadricula c = new Cuadricula(b);

	}

	@Test(expected = Exception.class)
	public void creoCuadriculaMenorUnoTest() {

		int b[] = { 0, 10 };
		@SuppressWarnings("unused")
		Cuadricula c = new Cuadricula(b);

	}

	@Test(expected = Exception.class)
	public void robotIniciaPosicionSuperiorTamanioCuadriculaTest() {

		int a[] = { 52, 5 };
		int b[] = { 50, 10 };
		Cuadricula c = new Cuadricula(b);
		@SuppressWarnings("unused")
		Robot r = new Robot(a, Sentido.OESTE, c);

	}

	@Test(expected = Exception.class)
	public void robotIniciaPosicionInferiorTamanioCuadriculaTest() {

		int a[] = { 0, 5 };
		int b[] = { 50, 10 };
		Cuadricula c = new Cuadricula(b);
		@SuppressWarnings("unused")
		Robot r = new Robot(a, Sentido.OESTE, c);

	}

}