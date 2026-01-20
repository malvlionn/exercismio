public class LogLevels {
    
    public static String message(String logLine) {
        int IndexSeparator = logLine.indexOf(":");
        return logLine.substring(IndexSeparator + 1).trim();
    }

    public static String logLevel(String logLine) {
        int kurungakhir = logLine.indexOf("]");
        return logLine.substring(1, kurungakhir).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
