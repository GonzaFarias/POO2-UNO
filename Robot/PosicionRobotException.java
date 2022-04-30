package practica;

@SuppressWarnings("serial")
public class PosicionRobotException extends RuntimeException {

	/**
	 * Esta expection se lanza cuando la posicion del robot no es compatible con el
	 * tamaño de la cuadricula.
	 * 
	 * @param s
	 */

	public PosicionRobotException(String s) {
		super(s);
	}
}