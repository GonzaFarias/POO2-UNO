package practica;

public class Cuadricula {
	private int cantidadFila;
	private int cantidadColumna;

	public Cuadricula(int[] datosCuadricula) throws MaximoMinimoCuadriculaException {
		if (datosCuadricula[0] < 1 || datosCuadricula[0] > 100 || 100 < datosCuadricula[1] || datosCuadricula[0] < 0) {
			throw new MaximoMinimoCuadriculaException("Los valores para crear la cuadricula son incorrectos");
		}
		this.cantidadFila = datosCuadricula[1];
		this.cantidadColumna = datosCuadricula[0];
	}

	public int getCantidadFila() {
		return cantidadFila;
	}

	public int getCantidadColumna() {
		return cantidadColumna;
	}

}