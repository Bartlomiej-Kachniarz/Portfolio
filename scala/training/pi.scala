import Console.{GREEN, RED, RESET, YELLOW_B, UNDERLINED}

object PrimeTest {

  def isPrime(): Unit = {

    val candidate = io.StdIn.readInt().ensuring(_ > 1)

    val prime = (2 to candidate - 1).forall(candidate % _ != 0)

    if (prime)
      Console.println(s"${RESET}${GREEN}yes${RESET}")
    else
      Console.err.println(s"${RESET}${YELLOW_B}${RED}${UNDERLINED}NO!${RESET}")
  }

  def main(args: Array[String]): Unit = isPrime()

}