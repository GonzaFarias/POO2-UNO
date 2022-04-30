package practica;

import java.util.ArrayList;

public class Robot {
	private int cantidadComandos = 0;
	private int posicionColumna;
	private int posicionFila;
	private Sentido sentido;
	private int limiteFila;
	private int limiteColumna;

	public Robot(int[] posicionesInicioRobot, Sentido sentidoInicio, Cuadricula cuadricula) {
		if (posicionesInicioRobot[1] > cuadricula.getCantidadFila() || posicionesInicioRobot[1] < 1) {
			throw new PosicionRobotException("La posicion de inicio del robot es menor o mayor a la cantidad de filas");
		}

		if (posicionesInicioRobot[0] > cuadricula.getCantidadColumna() || posicionesInicioRobot[0] < 1) {
			throw new PosicionRobotException(
					"La posicion de inicio del robot es menor o mayor a la cantidad de columnas");
		}
		this.posicionColumna = posicionesInicioRobot[0];
		this.posicionFila = posicionesInicioRobot[1];
		this.sentido = sentidoInicio;
		this.limiteFila = cuadricula.getCantidadFila();
		this.limiteColumna = cuadricula.getCantidadColumna();
	}

	public void instruccion(String caracter, int num) throws CantidadComandosException {

		cantidadComandos++;

		if (cantidadComandos > 125) {

			throw new CantidadComandosException("La cantidad de comandos no puede superar 125");

		}

		System.out.println("En sentido: "+this.sentido);
		System.out.println("Comando: " + caracter + num);

		if (caracter.equals("R")) {
			this.setSentido(this.rotar(num));

		} else if (caracter.equals("A")) {
			this.avanzar(num);

		} else
			System.err.println("Opción mal ingresada, solo se puede rotar (R) y avanzar (A)");

		System.out.println("Fila: " + this.posicionFila + " Columna: " + this.posicionColumna);
		System.out.println("------------");
	}

	public Sentido rotar(int n) {

		Sentido sentidoRetorno = null;

		if (n == 0 || n == 4 || n == 8) {
			sentidoRetorno = this.sentido;
		}

		if (n == 1 || n == 5 || n == 9) {

			if (this.sentido.equals(Sentido.NORTE)) {
				sentidoRetorno = Sentido.ESTE;
			}
			if (this.sentido.equals(Sentido.ESTE)) {
				sentidoRetorno = Sentido.SUR;
			}
			if (this.sentido.equals(Sentido.SUR)) {
				sentidoRetorno = Sentido.OESTE;
			}
			if (this.sentido.equals(Sentido.OESTE)) {
				sentidoRetorno = Sentido.NORTE;
			}
		}
		if (n == 2 || n == 6) {
			if (this.sentido.equals(Sentido.NORTE)) {
				sentidoRetorno = Sentido.SUR;
			}
			if (this.sentido.equals(Sentido.ESTE)) {
				sentidoRetorno = Sentido.OESTE;
			}
			if (this.sentido.equals(Sentido.SUR)) {
				sentidoRetorno = Sentido.NORTE;
			}
			if (this.sentido.equals(Sentido.OESTE)) {
				sentidoRetorno = Sentido.ESTE;
			}
		}
		if (n == 3 || n == 7) {
			if (this.sentido.equals(Sentido.NORTE)) {

				sentidoRetorno = Sentido.OESTE;
			}
			if (this.sentido.equals(Sentido.ESTE)) {
				sentidoRetorno = Sentido.NORTE;
			}
			if (this.sentido.equals(Sentido.SUR)) {
				sentidoRetorno = Sentido.ESTE;
			}
			if (this.sentido.equals(Sentido.OESTE)) {
				sentidoRetorno = Sentido.SUR;
			}

		}

		return sentidoRetorno;

	}

	public void avanzar(int n) {

		if (this.sentido.equals(Sentido.NORTE)) {
			if ((this.posicionFila + n) <= this.limiteFila) {
				this.setPosicionFila(this.posicionFila += n);
			} else {
				this.setPosicionFila(this.limiteFila);
			}
		}

		if (this.sentido.equals(Sentido.ESTE)) {
			if ((this.posicionColumna - n) >= 1) {
				this.setPosicionColumna(this.posicionColumna -= n);
			} else {
				this.setPosicionColumna(this.posicionColumna = 1);
			}
		}

		if (this.sentido.equals(Sentido.SUR)) {
			if ((this.posicionFila - n) >= 1) {
				this.setPosicionFila(this.posicionFila -= n);
			} else {
				this.setPosicionFila(this.posicionFila = 1);
			}

		}

		if (this.sentido.equals(Sentido.OESTE)) {
			if ((this.posicionColumna + n) <= this.limiteColumna) {
				this.posicionColumna += n;
			} else {
				this.posicionColumna = this.limiteColumna;
			}
		}

	}

	public void ejecutarInstrucciones(ArrayList<String> instrucciones) {
        for (int x = 0; x < instrucciones.size()-1; x+=2) {
            int num = Integer.parseInt(instrucciones.get(x+1));
            String caracter = instrucciones.get(x);
            this.instruccion(caracter, num);
        }
    }
	
	public Sentido getSentido() {
		return sentido;
	}

	public void setSentido(Sentido sentido) {
		this.sentido = sentido;
	}

	public int getPosicionColumna() {
		return posicionColumna;
	}

	public void setPosicionColumna(int posicionColumna) {
		this.posicionColumna = posicionColumna;
	}

	public int getPosicionFila() {
		return posicionFila;
	}

	public void setPosicionFila(int posicionFila) {
		this.posicionFila = posicionFila;
	}

}