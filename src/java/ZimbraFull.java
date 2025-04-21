import java.io.*;
import java.net.HttpURLConnection;
import java.net.URI;
//import java.net.URL;
import java.nio.file.*;
//import java.text.SimpleDateFormat;
import java.util.*;
import javax.xml.parsers.*;
import org.w3c.dom.*;
import org.xml.sax.InputSource;

public class ZimbraFull {

    private static final String ZIMBRA_SOAP_URL = "https://zimbra.tda-sgft.com/service/soap";
    private static final String CSV_PATH = "C:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD\\C_Export_CSV_Diario.csv";

    public static void main(String[] args) {
        try {
            System.out.println("Inicio del proceso...");

            // Paso 1: Leer CSV
            List<Map<String, String>> csvData = readCsv(CSV_PATH);
            if (csvData.isEmpty()) {
                System.out.println("No se encontraron datos en el CSV.");
                return;
            }

            // Paso 2: Crear token de autenticación
            String authToken = createAuthToken("carpios@tda-sgft.com", "G3m4198005&&");
            if (authToken == null) {
                System.out.println("Error al obtener el token de autenticación.");
                return;
            }

            // Paso 3: Crear una cita
            createAppointment(authToken, csvData);

            // Paso 4: Crear tareas
            createTasks(authToken, csvData);

            System.out.println("Proceso finalizado.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Paso 1: Leer CSV
    private static List<Map<String, String>> readCsv(String filePath) throws IOException {
        List<Map<String, String>> data = new ArrayList<>();
        try (BufferedReader br = Files.newBufferedReader(Paths.get(filePath))) {
            String[] headers = br.readLine().split(";");
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(";");
                Map<String, String> row = new HashMap<>();
                for (int i = 0; i < headers.length; i++) {
                    row.put(headers[i], values[i]);
                }
                data.add(row);
            }
        }
        return data;
    }

    // Paso 2: Crear token de autenticación
    private static String createAuthToken(String username, String password) throws Exception {
        String authXml = String.format(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
            + "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\">"
            + "<soap:Body>"
            + "<AuthRequest xmlns=\"urn:zimbraAccount\">"
            + "<account by=\"name\">%s</account>"
            + "<password>%s</password>"
            + "</AuthRequest>"
            + "</soap:Body>"
            + "</soap:Envelope>",
            username, password
        );

        String response = sendSoapRequest(ZIMBRA_SOAP_URL, authXml);
        return parseXmlForTag(response, "authToken");
    }

    // Paso 3: Crear una cita
    private static void createAppointment(String authToken, List<Map<String, String>> csvData) throws Exception {
        String title = "Cita de prueba";
        String startDate = "20250421T073000Z";
        String endDate = "20250421T093000Z";

        String appointmentXml = String.format(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
            + "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\">"
            + "<soap:Header>"
            + "<context xmlns=\"urn:zimbra\">"
            + "<authToken>%s</authToken>"
            + "</context>"
            + "</soap:Header>"
            + "<soap:Body>"
            + "<CreateAppointmentRequest xmlns=\"urn:zimbraMail\">"
            + "<m>"
            + "<inv method=\"REQUEST\" type=\"event\">"
            + "<comp name=\"%s\">"
            + "<s d=\"%s\"/>"
            + "<e d=\"%s\"/>"
            + "</comp>"
            + "</inv>"
            + "<su>%s</su>"
            + "<mp ct=\"text/plain\">"
            + "<content>Contenido de la cita</content>"
            + "</mp>"
            + "</m>"
            + "</CreateAppointmentRequest>"
            + "</soap:Body>"
            + "</soap:Envelope>",
            authToken, title, startDate, endDate, title
        );

        String response = sendSoapRequest(ZIMBRA_SOAP_URL, appointmentXml);
        System.out.println("Respuesta al crear cita: " + response);
    }

    // Paso 4: Crear tareas
    private static void createTasks(String authToken, List<Map<String, String>> csvData) throws Exception {
        for (Map<String, String> row : csvData) {
            String title = "Tarea: " + row.get("ASUNTO");
            String startDate = "20250421T073000Z";
            String endDate = "20250421T093000Z";

            String taskXml = String.format(
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
                + "<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\">"
                + "<soap:Header>"
                + "<context xmlns=\"urn:zimbra\">"
                + "<authToken>%s</authToken>"
                + "</context>"
                + "</soap:Header>"
                + "<soap:Body>"
                + "<CreateTaskRequest xmlns=\"urn:zimbraMail\">"
                + "<m>"
                + "<inv method=\"REQUEST\" type=\"task\">"
                + "<comp name=\"%s\">"
                + "<s d=\"%s\"/>"
                + "<e d=\"%s\"/>"
                + "</comp>"
                + "</inv>"
                + "<su>%s</su>"
                + "<mp ct=\"text/plain\">"
                + "<content>Contenido de la tarea</content>"
                + "</mp>"
                + "</m>"
                + "</CreateTaskRequest>"
                + "</soap:Body>"
                + "</soap:Envelope>",
                authToken, title, startDate, endDate, title
            );

            String response = sendSoapRequest(ZIMBRA_SOAP_URL, taskXml);
            System.out.println("Respuesta al crear tarea: " + response);
        }
    }

    // Método para enviar solicitudes SOAP
    private static String sendSoapRequest(String url, String xml) throws Exception {
        HttpURLConnection connection = (HttpURLConnection) URI.create(url).toURL().openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "text/xml");
        connection.setDoOutput(true);

        try (OutputStream os = connection.getOutputStream()) {
            os.write(xml.getBytes());
        }

        try (InputStream is = connection.getInputStream()) {
            return new String(is.readAllBytes());
        }
    }

    // Método para extraer un valor de un tag XML
    private static String parseXmlForTag(String xml, String tagName) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(new InputSource(new StringReader(xml)));
        NodeList nodes = doc.getElementsByTagName(tagName);
        return nodes.getLength() > 0 ? nodes.item(0).getTextContent() : null;
    }
}