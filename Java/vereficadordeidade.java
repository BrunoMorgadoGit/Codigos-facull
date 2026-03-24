import java.util.Scanner;

public class Main {
public static void main(String[] args) {
Scanner scanner = new Scanner([System.in](http://system.in/));

```
    System.out.print("Qual é o seu nome? ");
    String nome = scanner.nextLine();

    System.out.print("Quantos anos voce tem? ");
    float idade = scanner.nextFloat();
if (idade >= 18) {
	    System.out.println("Voce pode votar!!"); 
} else {
    System.out.println("Voce não pode votar!!");
}
    scanner.close();
}
```

}