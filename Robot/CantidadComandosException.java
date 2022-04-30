package practica;

@SuppressWarnings("serial")
public class CantidadComandosException extends RuntimeException {

	/**
	 * Exception lanzada cuando el robot llega al limite de comandos
	 * 
	 * @param s
	 */

	public CantidadComandosException(String s) {
		super(s);
	}
}
