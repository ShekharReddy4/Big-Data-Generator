import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.util.Random;
import java.util.Scanner;

public class TestDataGenerator {

    public static void main(String[] args) throws Exception{
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter input File name to get Account Name/Id");
        String s1 = scanner.nextLine();
        System.out.println("Please enter FROM date(in format YYYY-MM-DD) to generate Usage data");
        String s3 = scanner.nextLine();
        System.out.println("Please enter TO date(in format YYYY-MM-DD) to generate Usage data");
        String s4 = scanner.nextLine();
        System.out.println("Please enter FROM value to generate Integer Value");
        String FromInt = scanner.nextLine();
        int s5 = Integer.valueOf(FromInt);
        System.out.println("Please enter FROM value to generate Integer Value");
        String ToValue = scanner.nextLine();
        int s6 = Integer.valueOf(ToValue);
        Process p = Runtime.getRuntime().exec("python E:\\Spark\\test1.py "+s1+" "+s3+" "+s4+" "+s5+" "+s6);
        BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String ret = new String(in.readLine());
        System.out.println("Output Status : "+ret);
    }
}