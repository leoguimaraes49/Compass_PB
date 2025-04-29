// Etapa 4 – Contagem de palavras no README.md com Spark Shell (Scala)
// Instruções: dentro do container Docker já em execução, execute:
//   spark-shell
// e então cole este bloco no prompt scala> e pressione Enter:

sc.textFile("work/README.md")
  .flatMap(line => line.split("[^\p{L}]+"))   // separa só sequências de letras
  .filter(_.matches("\p{L}+"))                // filtra vazios e símbolos
  .map(_.toLowerCase)                          // normaliza em minúsculo
  .map(word => (word, 1))                      // mapeia cada palavra para (palavra, 1)
  .reduceByKey(_ + _)                          // soma as ocorrências
  .sortBy(_._2, ascending = false)             // ordena por frequência decrescente
  .take(20)                                    // mostra as 20 mais frequentes
  .foreach { case (w, c) => println(s"$w: $c") }