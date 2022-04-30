package practica;

@SuppressWarnings("serial")
public class MaximoMinimoCuadriculaException extends RuntimeException {

	/**
	 * Exception lanzada cuando la cuadricula se intenta crear con un tamaño
	 * 0>N,M>100
	 * 
	 * @param s
	 */

	public MaximoMinimoCuadriculaException(String s) {
		super(s);
	}
}
