import java.util.Scanner;

public class CalculadoraDeDescontoMain {
public static void main(String[] args) {

```
    Scanner scanner = new Scanner(System.in);

    System.out.print("Qual é o preço do Produto? ");
    String entradaPreco = scanner.nextLine();

    entradaPreco = entradaPreco.replace("R$", "").trim();
    float preco = Float.parseFloat(entradaPreco);

    System.out.print("Qual é o percentual de desconto do Produto? ");
    String entradaDesconto = scanner.nextLine();

    entradaDesconto = entradaDesconto.replace("%", "").trim();
    float desconto = Float.parseFloat(entradaDesconto);

    float resultado = preco - (preco * desconto /100);
    System.out.print("O valor a ser pago é R$ " + resultado);

    scanner.close();

}
```

}