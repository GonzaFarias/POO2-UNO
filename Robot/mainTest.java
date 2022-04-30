package practica;

import java.util.ArrayList;

public class mainTest {

public static void main(String[] args) throws Exception {
		
		
		Archivo a = new Archivo();
		a.leerArchivo("ROBOT.in");
		Cuadricula c = new Cuadricula(a.datosCuadricula());
		Robot r = new Robot(a.datosRobot(),a.tipoSentido(),c);
		ArrayList<String> instrucciones = a.instrucciones;
		
		r.ejecutarInstrucciones(instrucciones);

		a.escribirArchivo(r.getPosicionFila(), r.getPosicionColumna());
		
	}
}
