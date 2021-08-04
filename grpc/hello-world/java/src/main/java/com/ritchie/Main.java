package com.ritchie;

import com.ritchie.formula.Formula;

public class Main {

  public static void main(String[] args) {

    String username = System.getenv("RIT_USERNAME");
    String password = System.getenv("RIT_PASSWORD");

    Formula formula = new Formula(username, password);
    formula.Run();
  }
}
