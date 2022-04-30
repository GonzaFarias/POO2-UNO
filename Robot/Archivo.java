package practica;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Archivo {

	private int n, m, x, y;
	private String sentido;
	ArrayList<String> instrucciones = new ArrayList<String>();
	private String archivo = "";
	PrintWriter out;

	public Archivo() throws FileNotFoundException {
		this.archivo = "ROBOT.OUT";
		out = new PrintWriter(this.archivo);
	}

	public void leerArchivo(String archivo) throws Exception {

		Scanner s = new Scanner(new File(archivo));

		String[] arrDatos;
		int x = 0, y = 0, m = 0, n = 0;
		String sent = "";
		boolean flag = false;
		while (s.hasNext()) {

			if (!flag) {
				try {
					arrDatos = s.nextLine().split(" ");
					x = Integer.parseInt(arrDatos[0]);
					y = Integer.parseInt(arrDatos[1]);
					sent = arrDatos[2];
					n = Integer.parseInt(arrDatos[3]);
					m = Integer.parseInt(arrDatos[4]);
					if (100 < n || n < 0 || 100 < m || m < 0) {
						throw new MaximoMinimoCuadriculaException(
								"Los valores para crear la cuadricula son incorrectos");
					}
					this.m = m;
					this.n = n;
					this.x = x;
					this.y = y;
					if (this.x > this.n || this.x < 1) {
						throw new PosicionRobotException(
								"La posicion de inicio del robot es menor o mayor a la cantidad de columnas");
					}

					if (this.y > this.m || this.y < 1) {
						throw new PosicionRobotException(
								"La posicion de inicio del robot es menor o mayor a la cantidad de filas");
					}
					this.sentido = sent;

				} catch (ArrayIndexOutOfBoundsException a) {
					System.err.println("        Error: La cantidad de parametros dados no coinciden");
				}
				flag = true;
			} else {
				arrDatos = s.nextLine().split("");
				for (int i = 0; i < arrDatos.length; i++) {
					if (i % 2 != 0 && this.isInteger(arrDatos[i])) {
						instrucciones.add(arrDatos[i]);
					} else if (i % 2 == 0 && !this.isInteger(arrDatos[i])
							&& (arrDatos[i].equals("R") || arrDatos[i].equals("A"))) {

						instrucciones.add(arrDatos[i]);
					} else {
						throw new Exception("Comando mal indicado, corrija el ingreso e intente de nuevo.");
					}
				}
			}

		}
		s.close();

		System.out.println(
				"Posiciones: X: " + x + "  Y: " + y + "\nSentido inicial: " + sent + "\nTamaño cuadricula: N: " + n + "  M: " + m);

		for (x = 0; x < instrucciones.size(); x++) {
			System.out.print(instrucciones.get(x));
		}
		System.out.println("\n------------");
	}

	public boolean isInteger(String dato) {
		try {
			Integer.parseInt(dato);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}

	public int[] datosCuadricula() {

		int[] vector = new int[2];
		vector[0] = n;
		vector[1] = m;

		return vector;
	}

	public int[] datosRobot() {

		int[] vector = new int[2];
		vector[0] = x;
		vector[1] = y;

		return vector;
	}

	public Sentido tipoSentido() {

		if (this.sentido.equals("S")) {
			return Sentido.SUR;
		}
		if (this.sentido.equals("N")) {
			return Sentido.NORTE;
		}
		if (this.sentido.equals("O")) {
			return Sentido.OESTE;
		}
		if (this.sentido.equals("E")) {
			return Sentido.ESTE;
		}

		return null;

	}

	public ArrayList<String> instrucciones() {
		return this.instrucciones;
	}

	public void escribirArchivo(int x, int y) throws IOException {

		this.out.print(x+" "+y);
		this.out.close();
	}

}